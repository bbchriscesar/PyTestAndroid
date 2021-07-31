import pytest
from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import By


@pytest.fixture(scope="class")
def setup(request):
    global driver
    caps = {}
    caps["deviceName"] = "t650c"
    caps["udid"] = "860-012-054"
    caps["platformName"] = "Android"
    caps["platformVersion"] = "8.1.0"
    caps["automationName"] = "UiAutomator2"
    caps["appActivity"] = "com.global.fb.display.activities.DisplayModuleActivity"
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    driver.find_element_by_accessibility_id("Payments").click()
    request.cls.driver = driver
    yield
    driver.quit()
