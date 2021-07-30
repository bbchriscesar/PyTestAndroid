import pytest
from appium import webdriver


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
    caps["accessibilityId"] = "Settings"
    caps["ensureWebviewsHavePages"] = True
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    request.cls.driver = driver
    yield
    driver.quit()
