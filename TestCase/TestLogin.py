# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     TestLogin.py
   Author :        曾良均
   QQ:             277099728
   Date：          12/11/2023 3:50 PM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

import pytest
from Common.logins import *
from Common.Operator import *
import uiautomator2 as u2


class TestLogin(Operator):
    account = '//*[@resource-id="com.ForesightIntelligence.FleetIntelligence:id/action_bar_root"]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]'
    pwd = '//*[@resource-id="com.ForesightIntelligence.FleetIntelligence:id/action_bar_root"]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]'
    loginBtn = 'LOGIN'

    logo = '//*[@resource-id="com.ForesightIntelligence.FleetIntelligence:id/action_bar_root"]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]'
    logoutBtn = 'android.widget.Button'

    def login(self, username='zljun8210@live.cn', pwd='Win.12345'):
        self.input(self.account, username)
        self.input(self.pwd, pwd)
        self.click(self.loginBtn)
        time.sleep(2)
        # txt = self.driver(className=self.logoutBtn).get_text()
        txt = self.find_element(self.logoutBtn).get_text()
        self.click(self.logoutBtn)
        return txt

    def test_login(self):
        self.driver = u2.connect()
        self.driver.app_start("com.ForesightIntelligence.FleetIntelligence")
        self.driver.implicitly_wait(10)
        txt = self.login()

        self.driver.app_stop("com.ForesightIntelligence.FleetIntelligence")
        self.driver.app_clear("com.ForesightIntelligence.FleetIntelligence")

        assert txt == 'SIGN OUT'


if __name__ == '__main__':
    pytest.main(['-vs', 'TestLogin.py'])  # 主函数模式
