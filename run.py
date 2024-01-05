# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     run.py
   Author :        曾良均
   QQ:             277099728
   Date：          12/11/2023 2:30 PM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'
import pytest
import os


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--clean-alluredir', '--alluredir=allure-results'])
    os.system(r"copy environment.properties allure-results\\")
    os.system(r"allure generate -c -o Report\allure-report")
