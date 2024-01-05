# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Operator.py
   Author :        曾良均
   QQ:             277099728
   Date：          12/11/2023 2:32 PM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

import re
import uiautomator2 as u2


def device():
    driver = u2.connect()
    driver.app_start("com.ForesightIntelligence.FleetIntelligence")
    return driver


class Operator:
    driver = None

    def find_element(self, location, **kwargs):
        if str(location).startswith("com"):  # 若开头是com则使用ID定位
            return self.driver(resourceId=location)
        elif str(location).startswith("android"):
            if kwargs:
                return self.driver(className=location, index=kwargs.values())  # classname+index组合定位
            else:
                return self.driver(className=location)
        elif re.findall("//", str(location)):  # 若//开头则使用正则表达式匹配后用xpath定位
            return self.driver.xpath(location)
        else:  # 若以上两种情况都不是，则使用描述定位
            try:
                if kwargs:
                    # text+index组合定位，Fleet App上存在以图片或字体来表示功能按钮，如WO附件的图库、拍照、录像功能
                    return self.driver(text=location, index=kwargs.values())
                else:
                    return self.driver(text=location)
            except Exception:
                return self.driver(description=location)

    def click(self, location, **kwargs):
        if kwargs:
            self.find_element(location, index=kwargs.values()).click()
        else:
            self.find_element(location).click()

    def clear(self, location):
        self.find_element(location).clear_text()

    def input(self, location, txt):
        # self.clear(location)
        self.find_element(location).set_text(txt)
