import inspect
import logging
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys
import os


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler(loggerName + '.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyElementVisibility(self, locator):
        wait = WebDriverWait(self.driver, 60)
        try:
            element = wait.until(EC.visibility_of_element_located((locator[0], locator[1])))
            return element
        except NameError:
            sys.exit(1)

    def clickElement(self, locator):
        wait = WebDriverWait(self.driver, 60)
        try:
            element = wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
            element.click()
        except NameError:
            sys.exit(1)

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
