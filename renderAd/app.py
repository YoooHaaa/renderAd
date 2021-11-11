# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : client.py
# Time       ：2021/10/27 16:51
# Author     ：Yooha
"""


import uiautomator2 as u2
from shower import Show

class App:
    device = None


    @classmethod
    def init(cls):
        try:
            cls.device = u2.connect_usb()
            return True, ''
        except Exception as err:
            Show.error("App", "init", str(err))
            return False, str(err)


    @classmethod
    def start_app(cls, pkg):
        try:
            cls.device.app_start(pkg)
            Show.info("App", "start_app", '正在启动应用' + pkg)
            return True, ""
        except Exception as err:
            Show.error("App", "start_app", str(err))
            return False, str(err)


    @classmethod
    def stop_app(cls, pkg):
        try:
            cls.device.app_stop(pkg)
            Show.info("App", "stop_app", '正在关闭应用' + pkg)
            return True, ""
        except Exception as err:
            Show.error("App", "start_app", str(err))
            return False, str(err)


    @classmethod
    def home(cls):
        try:
            cls.device.press("home") # 模拟Home键
            return True, ""
        except Exception as err:
            Show.error("App", "home", str(err))
            return False, str(err)


    @classmethod
    def back(cls):
        try:
            cls.device.press("back") # 模拟点击返回键
            return True, ""
        except Exception as err:
            Show.error("App", "back", str(err))
            return False, str(err)



