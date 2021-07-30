from appium.webdriver.common.mobileby import By


class SettingsElements:

    def __init__(self, driver):
        self.driver = driver

    airplaneMode = (By.XPATH, "//android.widget.TextView[@text='Airplane mode']")
    appManagement = (By.XPATH, "//android.widget.TextView[@text='App management']")

    #def GoogleMail(self):
        #return self.driver.find_element(*GoogleHomepage.gmail)