# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     assetPage.py
   Author :        曾良均
   QQ:             277099728
   Date：          12/11/2023 5:34 PM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

from Common.Operator import *


class assetPage(Operator):
    asset_menu = "Manage Assets"

    add_btn = 'Add'  # Add 按钮
    search_inbox = '//android.widget.RelativeLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]'

    # Add Page
    save_btn = 'Save'

