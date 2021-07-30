from pageObjects.Oppo import SettingsElements
from utilities.BaseClass import BaseClass
import pytest
from time import sleep


@pytest.mark.testpage
class ClearSettingsCacheTests(BaseClass):

    def test_ClearSettingsCache(self):

        oppo = SettingsElements(self.driver)

        self.scroll(SettingsElements.airplaneMode, SettingsElements.appManagement)
        sleep(3)
