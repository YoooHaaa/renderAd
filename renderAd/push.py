# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : push.py
# Time       ：2021/10/27 16:51
# Author     ：Yooha
"""

import os
from global_value import GlobalValue
from shell import Shell

class Push:

    def __init__(self):
        pass

    @classmethod
    def push_white_list(cls):
        Shell.excute_adb("adb push " + GlobalValue.current_path + "/resource/push/_white_list.config /data/local/tmp")

    @classmethod
    def push_twitter_js(cls):
        Shell.excute_adb("adb push " + GlobalValue.current_path + "/resource/push/twitter.js /data/local/tmp/frida_scripts")

    @classmethod
    def push_twitter_config(cls):
        Shell.excute_adb("adb push " + GlobalValue.current_path + "/resource/push/twitter.config /data/local/tmp/frida_scripts")

    @classmethod
    def push_dex(cls):
        Shell.excute_adb("adb push " + GlobalValue.current_path + "/resource/push/yooha.dex /data/local/tmp")

