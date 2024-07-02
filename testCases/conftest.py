import pytest
from selenium import webdriver
import os
from datetime import datetime

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FfService
from selenium.webdriver.firefox.options import Options as Ffoptions

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture()
def setup(browser):

    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--headless') --- for headless mode
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    options = webdriver.ChromeOptions()
    # prefs = {"download.default_directory":"C:\\Users\\varun\\OneDrive\\Desktop\\sarvahaAssignments"}
    # options.add_experimental_option("prefs", prefs)

    yield driver  # Provide the driver to the test
    driver.quit()  # Teardown


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime(
        "%d-%m-%Y %H-%M-%S") + ".html"
