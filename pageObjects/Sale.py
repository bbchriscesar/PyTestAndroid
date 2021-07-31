from appium.webdriver.common.mobileby import By


class SaleElements:

    def __init__(self, driver):
        self.driver = driver

    saleIdle = (By.XPATH, "//android.widget.TextView[@text='SALE']")
    cardVerificationIdle = (By.XPATH, "//android.widget.TextView[@text='CARD VERIFICATION']")
    giftIdle = (By.XPATH, "//android.widget.TextView[@text='GIFT']")
    refundIdle = (By.XPATH, "//android.widget.TextView[@text='REFUND']")
    padOne = (By.ID, "com.global.wwca:id/btn_number_one")
    okayButton = (By.XPATH, "(//android.widget.ImageButton[@content-desc='Image button footer'])[3]")
    accountNumberInput = (By.ID, "com.global.wwca:id/et_input_address")

    def sale(self):
        return self.driver.find_element(*SaleElements.saleIdle)