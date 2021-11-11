# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : shell.py
# Time       ：2021/10/27 16:51
# Author     ：Yooha
"""


import subprocess

class Shell:

    def __init__(self):
        pass


    @classmethod
    def excute_adb(cls, cmd:str) -> list:
        '''
        function:  执行单条 adb 命令，并获取命令行返回值
        '''
        try:
            obj = subprocess.Popen(cmd, shell = True, stdin=subprocess.PIPE, stdout=subprocess.PIPE ,stderr=subprocess.PIPE)
            info = obj.stdout.readlines()
        except Exception as err:
            return False, str(err)
        return True, str(info)

    @classmethod
    def excute_adb_shell(cls, cmd:list) -> list:
        '''
        function:  执行多条 adb shell 命令，并获取命令行返回值, 注意每条指令必须以\n结尾，['su\n', 'cd /data/local/tmp\n']
        '''
        info = None
        try:
            obj = subprocess.Popen(['adb', 'shell'], shell = True, stdin=subprocess.PIPE, stdout=subprocess.PIPE ,stderr=subprocess.PIPE)
            for line in cmd:
                obj.stdin.write(line.encode('utf-8'))
            info,err = obj.communicate()
        except Exception as err:
            return False, str(err)
        return True, (str(info.decode('gbk'))).split('\n')





