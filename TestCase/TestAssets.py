# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     TestAssets.py
   Author :        曾良均
   QQ:             277099728
   Date：          12/11/2023 5:30 PM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

import time

import pytest
from Common.logger import Log
from Common.logins import logins
import uiautomator2 as u2
from Page.assetPage import assetPage

log = Log("TestAssets")


@pytest.fixture()
def begin():
    driver = u2.connect()
    driver.app_start("com.ForesightIntelligence.FleetIntelligence")
    driver.implicitly_wait(10)
    lg = logins()
    lg.login(driver, username='admin@iicon004.com', pwd='Win.12345')
    lg.asset = assetPage()

    yield lg
    driver.app_stop("com.ForesightIntelligence.FleetIntelligence")
    driver.app_clear("com.ForesightIntelligence.FleetIntelligence")


@pytest.mark.usefixtures("begin")
class TestAssets:
    def add_asset(self, begin):
        time.sleep(3)
        begin.click(begin.asset.asset_menu)
        time.sleep(2)
        txt = begin.find_element(begin.asset.add_btn).get_text()
        return txt

    def test_asset(self, begin):
        res = self.add_asset(begin)
        assert res == 'Add'


if __name__ == '__main__':
    pytest.main(['-vs', 'TestAssets.py'])  # 主函数模式
