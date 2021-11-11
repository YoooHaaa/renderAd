# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : client.py
# Time       ：2021/10/29 14:24
# Author     ：Yooha
"""

import json
from push import Push
from  global_value import GlobalValue
from app import App
from shower import Show
import os

class Init:
    data = None

    @classmethod
    def init(cls):
        cls.init_forward()
        cls.init_global()
        cls.init_config()
        cls.init_app()

    
    @classmethod
    def init_global(cls):
        GlobalValue.init_value()
        Show.info('Init', 'init_global', "全局变量初始化完成")


    @classmethod
    def init_app(cls):
        App.init()
        Show.info('Init', 'init_app', "uiautomator2初始化完成")


    @classmethod
    def init_forward(cls):
        os.system("adb forward tcp:30000 tcp:30000")
        Show.info('Init', 'init_forward', "30000端口转发完成")

    @classmethod
    def init_config(cls):
        with open(GlobalValue.current_path + "/resource/config.json", "r", encoding='utf-8') as f:
            cls.data = json.load(f)
        if not cls.data["init"]:
            Push.push_dex()
            #Push.push_twitter_config()
            Push.push_twitter_js()
            #Push.push_white_list()
            cls.data["init"] = True
            with open(GlobalValue.current_path + "/resource/config.json", "w", encoding='utf-8') as f:
                json.dump(cls.data, f)
        Show.info('Init', 'init_config', "config初始化完成")




