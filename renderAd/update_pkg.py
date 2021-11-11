# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : update_pkg.py
# Time       ：2021/11/2 10:32
# Author     ：Yooha
"""

import os
from global_value import GlobalValue
from push import Push
import json

class UpdatePkg:

    def __init__(self):
        pass

    @classmethod
    def update_white(cls, pkg):
        with open(GlobalValue.current_path + "/resource/push/_white_list.config", "w", encoding='utf-8') as f:
            f.write(pkg)

    @classmethod
    def update_twitter(cls, pkg):
        data = None
        with open(GlobalValue.current_path + "/resource/push/twitter.config", "r", encoding='utf-8') as f:
            data = json.load(f)
        data["filter"]["bundles"][0] = pkg
        with open(GlobalValue.current_path + "/resource/push/twitter.config", "w", encoding='utf-8') as f:
            json.dump(data, f)

    @classmethod
    def update(cls, pkg):
        cls.update_white(pkg)
        cls.update_twitter(pkg)
        Push.push_white_list()
        Push.push_twitter_config()




