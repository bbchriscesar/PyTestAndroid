import pytest
from pageObjects.Sale import SaleElements
from utilities.BaseClass import BaseClass
from time import sleep


@pytest.mark.sale
class SaleTransactionTests(BaseClass):

    def test_saleTransaction(self):

        sale = SaleElements(self.driver)
        log = self.getLogger()

        # Verify SALE is present
        self.verifyElementVisibility(sale.saleIdle)
        log.info("Verify SALE is present")

        # Verify CARD VERIFICATION is present
        self.verifyElementVisibility(sale.cardVerificationIdle)
        log.info("Verify CARD VERIFICATION is present")

        # Verify GIFT is present
        self.verifyElementVisibility(sale.giftIdle)
        log.info("Verify GIFT is present")

        # Verify REFUND is present
        self.verifyElementVisibility(sale.refundIdle)
        log.info("Verify REFUND is present")

        # Tap SALE button
        self.clickElement(sale.saleIdle)
        log.info("Tap SALE button")

        # Enter amount
        self.clickElement(sale.padOne)
        log.info("Enter amount")

        # Tap OKAY button
        self.clickElement(sale.okayButton)
        log.info("Tap OKAY button")

        # Enter Tax Amount
        self.clickElement(sale.padOne)
        log.info("Enter Tax Amount")

        # Tap OKAY button
        self.clickElement(sale.okayButton)
        log.info("Tap OKAY button")

        # Enter Tip Amount
        self.clickElement(sale.padOne)
        log.info("Enter Tip Amount")

        # Tap OKAY button
        self.clickElement(sale.okayButton)
        log.info("Tap OKAY button")

        # Tap OKAY button
        self.clickElement(sale.okayButton)
        log.info("Tap OKAY button")

        # Tap OKAY button
        self.clickElement(sale.okayButton)
        log.info("Tap OKAY button")
        sleep(5)