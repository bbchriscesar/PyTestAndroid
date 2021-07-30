import pytest
from appium import webdriver
from time import sleep


@pytest.fixture(scope="class")
def setup(request):
    global driver
    caps = {}
    caps["deviceName"] = "OPPO A5s"
    caps["udid"] = "Q4QSQCYSLJ65JZSC"
    caps["platformName"] = "Android"
    caps["platformVersion"] = "8"
    caps["automationName"] = "UiAutomator2"
    caps["appActivity"] = "com.oppo.settings.SettingsActivity"
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    sleep(3)
    driver.find_element_by_xpath("//android.widget.TextView[@text='Settings']").click()
    request.cls.driver = driver
    yield
    driver.quit()
