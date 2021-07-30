import inspect
import logging
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def checkElementVisibility(self, locator):
        wait = WebDriverWait(self.driver, 60)
        try:
            element = wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
            return element
        except Exception as ex:
            print(ex)

    def clickElement(self, locator):
        wait = WebDriverWait(self.driver, 30)
        try:
            element = wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
            element.click()
        except Exception as ex:
            print(ex)

    def sendKeys(self, locator, value):
        wait = WebDriverWait(self.driver, 30)
        try:
            element = wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
            element.clear()
            element.send_keys(value, Keys.ENTER)
        except Exception as ex:
            print(ex)

    def scroll(self):
        sleep(3)
        self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"App management\"))")