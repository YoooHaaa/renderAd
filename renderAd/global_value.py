# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : setting.py
# Time       ：2021/10/27 15:50
# Author     ：Yooha
"""


import time
import threading
import os
import sys

class GlobalValue():
    global_time = None
    threadLock = None
    isLive = None
    current_path = None
    

    def __init__(self):
        pass

    @classmethod
    def init_value(cls):
        cls.global_time = time.time()
        cls.threadLock = threading.Lock()
        cls.isLive = False
        cls.current_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    @classmethod
    def init_time(cls):
        cls.global_time = time.time()


msg_template = {
    "type":"",
    "event":"",
    "msg":"msg from Android",
    "status":"100"
}
