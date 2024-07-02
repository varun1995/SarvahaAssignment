from selenium.webdriver.common.by import By


class FileDownloadPage:
    btn_acceptCookies = "accept-cookie-notification"
    icon_csvFile = ".icon-csv"

    inp_subscribe = "subscribeEmail"
    btn_subscribe = "//input[@id='subscribeToPage']"
    txt_subscribe_invalid_email = "//div[@class='error-msg show']/div/span"
    txt_subscribe_success = "//div[@class='success-bar']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, usrEmail):
        self.driver.find_element(By.ID, self.inp_subscribe).send_keys(usrEmail)

    def clickSubscribeBtn(self):
        self.driver.find_element(By.XPATH, self.btn_subscribe).click()

    def getConfirmationMsg(self):
        return self.driver.find_element(By.XPATH, self.txt_subscribe_success).text

    def acceptCookies(self):
        self.driver.find_element(By.ID, self.btn_acceptCookies).click()

    def downloadCsvFile(self):
        self.driver.find_element(By.CSS_SELECTOR, self.icon_csvFile).click()
