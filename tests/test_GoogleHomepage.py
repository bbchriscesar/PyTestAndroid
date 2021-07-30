from pageObjects.Oppo import SettingsElements
from utilities.BaseClass import BaseClass
import pytest
from time import sleep


@pytest.mark.clearcache
class ClearSettingsCacheTests(BaseClass):

    def test_ClearSettingsCache(self):

        oppo = SettingsElements(self.driver)

        self.scroll()
        self.clickElement(oppo.appManagement)
        sleep(3)
