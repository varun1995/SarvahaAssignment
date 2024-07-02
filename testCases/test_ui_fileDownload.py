from pageObjects.FileDownloadPage import FileDownloadPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os, time
import pytest


class Test_File_Download_Page():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger
    download_dir = "C:\\Users\\varun\\Downloads"  # Download directory

    @pytest.mark.sanity
    @pytest.mark.parametrize('usrEmail', ['abc123@gmail.com', '67890'])
    def test_subscribeFunction(self, setup, usrEmail):
        self.logger.info("******* Starting subscription test **********")
        self.driver = setup

        try:
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            self.fdp = FileDownloadPage(self.driver)
            self.logger.info("Entering email id for subscription")
            self.fdp.setEmail(usrEmail)
            self.fdp.clickSubscribeBtn()

            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, self.fdp.txt_subscribe_success),
                                                 "Thank you, you have been successfully subscribed.")
            )

            self.confmsg = self.fdp.getConfirmationMsg()
            if self.confmsg == "Thank you, you have been successfully subscribed.":
                self.logger.info("Subscription done successfully!!")
                self.driver.save_screenshot(
                    os.path.abspath(os.curdir) + "\\screenshots\\" + "test_subscribeFunction_success.png")
                assert True

            else:
                raise Exception("Subscription message mismatch.")

        except Exception as e:
            self.logger.error(f"Subscription failed!! Error: {str(e)}")
            screenshot_dir = os.path.join(os.path.abspath(os.curdir), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            self.driver.save_screenshot(os.path.join(screenshot_dir, "test_subscribeFunction_failure.png"))
            assert False
        finally:
            self.logger.info("******* Ending subscription test **********")

    @pytest.mark.regression
    def test_fileDownload(self, setup):
        self.logger.info("******* Starting file download test **********")
        self.driver = setup

        try:
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            self.fdp = FileDownloadPage(self.driver)

            # self.fdp.acceptCookies()
            self.fdp.downloadCsvFile()
            file_name = "BrowserStack - List of devices to test on.csv"
            file_path = os.path.join(self.download_dir, file_name)
            self.logger.info(file_path)

            # Wait for the file to be downloaded
            wait_time = 10  # Max wait time in seconds
            start_time = time.time()
            while not os.path.exists(file_path):
                if time.time() - start_time > wait_time:
                    raise Exception("File download timed out.")
                time.sleep(1)  # Wait for 1 second before checking again

            self.logger.info("File downloaded successfully.")
        except Exception as e:
            self.logger.fatal(f"An error occurred: {str(e)}")
        finally:
            self.logger.info("******* End of file download test **********")
