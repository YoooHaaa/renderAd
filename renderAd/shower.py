# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : client.py
# Time       ：2021/10/28 11:21
# Author     ：Yooha
"""


import click
import datetime
import os
from global_value import GlobalValue

class Show(object):
    

    # blue  green   white  red   yellow
    @classmethod
    def error(cls, clsz, func, err):
        click.secho('%-30s%-30s%-20s' %(clsz, func, err), fg='red')
        if not os.path.exists(GlobalValue.current_path + "/error"):
            os.mkdir("./error")
        with open(GlobalValue.current_path + "/error/err.txt", "a", encoding='utf-8') as log:
            log.write("********************************************************************************\n")
            log.write(str(datetime.datetime.now()))
            log.write("\n")
            log.write(clsz + ' -> ' + func)
            log.write("\n")
            log.write(err)
            log.write("\n")


    @classmethod
    def warning(cls, clsz, func, war):
        click.secho('%-30s%-30s%-20s' %(clsz, func, war), fg='yellow')


    @classmethod
    def info(cls, clsz, func, inf):
        click.secho('%-30s%-30s%-20s' %(clsz, func, inf), fg='white')

