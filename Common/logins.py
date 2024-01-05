# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     logins.py
   Author :        曾良均
   QQ:             277099728
   Date：          12/11/2023 2:47 PM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

from Common.Operator import *
import time
import sys


class logins(Operator):
    account = '//*[@resource-id="com.ForesightIntelligence.FleetIntelligence:id/action_bar_root"]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]'
    pwd = '//*[@resource-id="com.ForesightIntelligence.FleetIntelligence:id/action_bar_root"]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]'
    loginBtn = 'LOGIN'

    logo = '//*[@resource-id="com.ForesightIntelligence.FleetIntelligence:id/action_bar_root"]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]'
    logoutBtn = 'android.widget.Button'

    def login(self, driver, username='zljun8210@live.cn', pwd='Win.12345'):
        # wait login page
        self.driver = driver
        self.input(self.account, username)
        self.input(self.pwd, pwd)
        self.click(self.loginBtn)

        time.sleep(2)
        try:
            self.find_element(self.logo).click()
        except Exception:
            sys.stderr.write("\nlogin failed!\n")
