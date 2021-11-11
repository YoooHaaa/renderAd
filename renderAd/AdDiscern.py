# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : AdDiscern.py
# Time       ：2021/9/14 11:51
# Author     ：Yooha
"""


import PyQt5
import sys
import time
import json
from PyQt5.QtGui import QStandardItem,QStandardItemModel
import datetime
import os
from global_value import GlobalValue
from PyQt5 import QtCore, QtWidgets
import PyQt5
from PyQt5.QtWidgets import QMessageBox
from app import App
import socket
import threading
from shower import Show
from init import Init
from update_pkg import UpdatePkg


# 1-监控中  2-正在加载  3-error  4-心跳包
JS_MONITOR = "监控中"
JS_LOAD    = "加载中"
JS_ERROR   = "Error"
JS_HEART   = "heartbeat"




#***********************************************************************************

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.label.setObjectName("label")
        self.edt_pkgname = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_pkgname.setGeometry(QtCore.QRect(80, 30, 201, 20))
        self.edt_pkgname.setObjectName("edt_pkgname")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 100, 51, 16))
        self.label_5.setObjectName("label_5")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(300, 30, 111, 21))
        self.btn_start.setObjectName("btn_start")
        self.btn_screenshot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_screenshot.setGeometry(QtCore.QRect(910, 30, 141, 23))
        self.btn_screenshot.setObjectName("btn_screenshot")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(880, 20, 20, 51))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 30, 81, 16))
        self.label_6.setObjectName("label_6")
        self.edt_platfrom = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_platfrom.setGeometry(QtCore.QRect(570, 30, 171, 20))
        self.edt_platfrom.setObjectName("edt_platfrom")
        self.btn_platfrom = QtWidgets.QPushButton(self.centralwidget)
        self.btn_platfrom.setGeometry(QtCore.QRect(760, 30, 101, 23))
        self.btn_platfrom.setObjectName("btn_platfrom")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(700, 100, 51, 16))
        self.label_7.setObjectName("label_7")
        self.tb_load = QtWidgets.QTableView(self.centralwidget)
        self.tb_load.setGeometry(QtCore.QRect(350, 120, 341, 561))
        self.tb_load.setObjectName("tb_load")
        self.tb_click = QtWidgets.QTableView(self.centralwidget)
        self.tb_click.setGeometry(QtCore.QRect(700, 120, 361, 561))
        self.tb_click.setObjectName("tb_click")
        self.tb_monitor = QtWidgets.QTableView(self.centralwidget)
        self.tb_monitor.setGeometry(QtCore.QRect(10, 120, 331, 561))
        self.tb_monitor.setObjectName("tb_monitor")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 80, 1051, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 0, 1051, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(440, 20, 20, 51))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1070, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RenderAdMonitor"))
        self.label.setText(_translate("MainWindow", "应用包名"))
        self.label_4.setText(_translate("MainWindow", "监控事件"))
        self.label_5.setText(_translate("MainWindow", "加载事件"))
        self.btn_start.setText(_translate("MainWindow", "开始监控"))
        self.btn_screenshot.setText(_translate("MainWindow", "截图"))
        self.label_6.setText(_translate("MainWindow", "新增聚合平台"))
        self.btn_platfrom.setText(_translate("MainWindow", "点击添加"))
        self.label_7.setText(_translate("MainWindow", "点击事件"))



class WindowAction(PyQt5.QtWidgets.QMainWindow):
    
    def __init__(self, render:object):
        super(WindowAction, self).__init__()
        self.render:AdRender = render
        self.client = None
        self.live = None


    def click_start(self):
        pkgname = self.render.ui.edt_pkgname.text()
        if pkgname == '':
            QMessageBox.warning(self,"警告", '请输入包名',QMessageBox.Ok)
            return   
        AdRender.init_pkgname(pkgname)   

        UpdatePkg.update(pkgname)

        self.render.clear_list_monitor()
        self.render.clear_list_load()
        self.render.clear_list_click()

        try:
            GlobalValue.init_time()
            App.stop_app(pkgname) 
            ret, info = App.start_app(pkgname) 
            if not ret:
                QMessageBox.critical(self, "错误", info, QMessageBox.Ok)
        except Exception as err:
            QMessageBox.critical(self, "错误", str(err), QMessageBox.Ok)

        try:
            if self.client:
                self.client.set_stop(True)
            if self.live:
                self.live.set_stop(True)
        except Exception as err:
            QMessageBox.critical(self, "错误", str(err), QMessageBox.Ok)

        time.sleep(3) # 延时1秒后，客户端开始连接
        self.client = mySocketClientThread(self.render)
        self.client.setDaemon(True) # 设置为守护线程，防止主线程退出，子线程还在跑
        self.client.start()
        self.live = CheckConnect(self.render)
        self.live.signal_error.connect(self.show_error_box)
        self.live.start()
        

    def click_add(self):
        self.render.updata_config(self.render.ui.edt_platfrom.text())


    def click_screenshot(self):
        ret, info = self.render.save_screenshot(self.render.ui.edt_pkgname.text())
        if ret:
            QMessageBox.information(self,"提示", '截图保存于' + info,QMessageBox.Ok)
        else:
            QMessageBox.critical(self,"错误", '截图失败',QMessageBox.Ok)


    def show_info_box(self, info):
        try:
            QMessageBox.information(self,"提示",  info, QMessageBox.Ok)
        except Exception as err:
            Show.error("WindowAction", "show_info_box", str(err))


    def show_error_box(self, err):
        try:
            QMessageBox.critical(self,"错误", err,QMessageBox.Ok)
        except Exception as err:
            Show.error("WindowAction", "show_info_box", str(err))
#***********************************************************************************


class CheckConnect(QtCore.QThread):       # 此线程中要改变ui，所以继承了 QtCore.QThread
    signal_error = QtCore.pyqtSignal(str) # 此信号必须定义为类属性

    def __init__(self, render, parent=None):
        super().__init__(parent)
        self.render:AdRender = render
        self.stop = False
        
    def run(self):
        '''
        function: 检查连接是否断开
        '''
        Show.info('CheckConnect', 'run', "正在创建查活线程")
        time.sleep(3)
        while True:
            if self.stop:
                break
            time.sleep(2)
            try:
                # 线程同步
                GlobalValue.threadLock.acquire()
                interval = time.time() - GlobalValue.global_time
                GlobalValue.threadLock.release()
                if interval > 20:
                    print(interval)
                    GlobalValue.isLive = False
                    Show.warning('CheckConnect', 'run', '连接已断开')
                    self.signal_error.emit('连接已断开，请重新连接')  # 发送信号，通知被绑定函数，来改变UI
                    return 
                else:
                    GlobalValue.isLive = True
                    Show.info('CheckConnect', 'run', '持续连接中')
            except Exception as err:
                Show.error('CheckConnect', 'run', str(err))

    def set_stop(self, flag):
        self.stop = flag




#***********************************************************************************
class mySocketClientThread (threading.Thread):
    

    def __init__(self, render):
        threading.Thread.__init__(self)
        self.socket = socket.socket()
        self.render:AdRender = render
        self.stop = False

    @classmethod
    def get_socket(cls):
        return cls.socket


    def run(self):
        try: 
            Show.info('mySocketClientThread', 'run', "正在建立新的连接")
            self.socket = socket.socket()
            self.socket.connect(('127.0.0.1',30000))  # 不阻塞
            self.socket.send("connect".encode('utf-8'))
            while True:
                if self.stop:
                    break
                try:
                    msg = self.socket.recv(4096).decode('utf-8')
                    if msg != "":
                        try:
                            info = json.loads(msg)
                            self.render.parse(info)
                            if info["msg"] == "heartbeat":
                                self.update_status()
                        except Exception as e:
                            Show.error('mySocketClientThread', 'run-1', str(e))
                except Exception as er:
                    Show.error('mySocketClientThread', 'run-2', str(er))
                    return
        except Exception as err:
            Show.error('mySocketClientThread', 'run-3', str(err))
            return


    def set_stop(self, flag):
        self.stop = flag

    def close(self):
        self.socket.close()


    def update_status(self):
        GlobalValue.threadLock.acquire()
        GlobalValue.global_time = time.time()
        GlobalValue.threadLock.release()
#***********************************************************************************
class AdRender(object):

    def __init__(self):
        self.init()


    @classmethod
    def init(cls):
        cls.application = PyQt5.QtWidgets.QApplication(sys.argv)
        cls.ui = Ui_MainWindow()
        cls.window = WindowAction(cls)
        cls.current_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        cls.window.setWindowIcon(PyQt5.QtGui.QIcon(cls.current_path + '/resource/icon.png'))
        cls.ui.setupUi(cls.window)
        Init.init()
        # 监控区
        cls.list_monitor_title_sdk_model = QStandardItemModel()
        cls.list_monitor_title_event_model = QStandardItemModel()
        cls.list_monitor_sdk_model = QStandardItemModel()
        cls.list_monitor_event_model = QStandardItemModel()
        # 加载区
        cls.list_load_title_sdk_model = QStandardItemModel()
        cls.list_load_title_event_model = QStandardItemModel()
        cls.list_load_sdk_model = QStandardItemModel()
        cls.list_load_event_model = QStandardItemModel()
        # 点击区
        cls.list_click_title_sdk_model = QStandardItemModel()
        cls.list_click_title_event_model = QStandardItemModel()
        cls.list_click_sdk_model = QStandardItemModel()
        cls.list_click_event_model = QStandardItemModel()

        cls.pkgname:str = ''
        cls.isPlatfrom:bool = False
        cls.current_sdk:str = ''
        cls.config:list = cls.get_config()
        cls.setup_action()
        cls.setup_tableModel()
        cls.window.show()
        sys.exit(cls.application.exec_())


    @classmethod
    def get_config(cls):
        with open(cls.current_path + "/resource/config.json", "r", encoding='utf-8') as f:
            return json.load(f)


    @classmethod
    def updata_config(cls, info):
        if info not in cls.config['platfrom']:
            cls.config['platfrom'].append(info)
        with open(cls.current_path + "/resource/config.json", "w", encoding='utf-8') as f:
            json.dump(cls.config, f)


    @classmethod
    def init_pkgname(cls, pkg):
        cls.pkgname = pkg
        cls.isPlatfrom = False
        cls.current_sdk = ''
        if not os.path.exists(cls.current_path + "/output/" + pkg):
            os.mkdir(cls.current_path + "/output/" + pkg)


    @classmethod
    def setup_tableModel(cls):
        # 监控区
        cls.ui.tb_monitor.setModel(PyQt5.QtGui.QStandardItemModel(cls.ui.tb_monitor))
        cls.ui.tb_monitor.model().setHorizontalHeaderLabels(['SDK', '事件'])
        cls.ui.tb_monitor.setColumnWidth(0, 150)
        cls.ui.tb_monitor.setColumnWidth(1, 230)
        # 加载区
        cls.ui.tb_load.setModel(PyQt5.QtGui.QStandardItemModel(cls.ui.tb_load))
        cls.ui.tb_load.model().setHorizontalHeaderLabels(['SDK', '事件'])
        cls.ui.tb_load.setColumnWidth(0, 150)
        cls.ui.tb_load.setColumnWidth(1, 220)
        # 点击区
        cls.ui.tb_click.setModel(PyQt5.QtGui.QStandardItemModel(cls.ui.tb_click))
        cls.ui.tb_click.model().setHorizontalHeaderLabels(['SDK', '事件'])
        cls.ui.tb_click.setColumnWidth(0, 150)
        cls.ui.tb_click.setColumnWidth(1, 230)


    @classmethod
    def add_list_monitor(cls, sdk, event):
        cls.ui.tb_monitor.model().appendRow([QStandardItem(sdk), QStandardItem(event)])

    @classmethod
    def clear_list_monitor(cls):
        while True:
            rootIndex = cls.ui.tb_monitor.model().index(0, 0) 
            if rootIndex.data() != None:
                cls.ui.tb_monitor.model().removeRow(rootIndex.row(), rootIndex.parent())
            else:
                break
        
    @classmethod
    def add_list_load(cls, sdk, event):
        cls.ui.tb_load.model().appendRow([QStandardItem(sdk), QStandardItem(event)])


    @classmethod
    def clear_list_load(cls):
        while True:
            rootIndex = cls.ui.tb_load.model().index(0, 0) 
            if rootIndex.data() != None:
                cls.ui.tb_load.model().removeRow(rootIndex.row(), rootIndex.parent())
            else:
                break

    @classmethod
    def add_list_click(cls, sdk, event):
        cls.ui.tb_click.model().appendRow([QStandardItem(sdk), QStandardItem(event)])

    @classmethod
    def clear_list_click(cls):
        while True:
            rootIndex = cls.ui.tb_click.model().index(0, 0) 
            if rootIndex.data() != None:
                cls.ui.tb_click.model().removeRow(rootIndex.row(), rootIndex.parent())
            else:
                break

    @classmethod
    def setup_action(cls):
        cls.ui.btn_start.clicked.connect(cls.window.click_start)
        cls.ui.btn_platfrom.clicked.connect(cls.window.click_add)
        cls.ui.btn_screenshot.clicked.connect(cls.window.click_screenshot)

    @classmethod
    def parse(cls, data):
        type, event, status, msg = data['type'], data['event'], data['status'], data['msg']
        if status == JS_MONITOR:
            cls.add_list_monitor(type, event)
        if status == JS_LOAD:
            if not cls.isPlatfrom:
                cls.is_platfrom(msg)
            if not cls.isPlatfrom:
                if event.find('加载') != -1:
                    cls.add_list_load(type, event)
                else:
                    cls.add_list_click(type, event)
                cls.save_stack(type, event, msg)
            else:
                if event.find('加载') != -1:
                    cls.add_list_load('聚合平台' + cls.current_sdk, event)
                else:
                    cls.add_list_click('聚合平台' + cls.current_sdk, event)
                cls.save_stack(type, event, msg)
        if status == JS_ERROR:
            cls.add_list_monitor(type + '(监控失败)', event)
        if JS_HEART == status:
            GlobalValue.global_time = time.time()


    @classmethod
    def is_platfrom(cls, msg):
        for item in cls.config['platfrom']:
            if msg.find(item) != -1:
                cls.isPlatfrom = True
                cls.clear_list_load()
                cls.clear_list_click()
                cls.current_sdk = item

    @classmethod
    def save_stack(cls, sdk, event, stack): 
        with open(cls.current_path + "/output/" + cls.pkgname + "/" + cls.pkgname + ".txt", "a", encoding='utf-8') as log:
            log.write("********************************************************************************\n")
            log.write(str(datetime.datetime.now()))
            log.write("\n")
            log.write(sdk)
            log.write("\n")
            log.write(event)
            log.write("\n")
            log.write(stack)
            log.write("\n")

    @classmethod
    def save_screenshot(cls, pkgname): 
        try:
            filename = cls.format_time() + ".png"
            os.system("adb shell screencap -p /sdcard/" + filename)
            os.system("adb pull /sdcard/" + filename + " " + cls.current_path + "/output/" + pkgname + '/')  
        except Exception as err:
            Show.error('AdRender', 'save_screenshot', str(err))
            return False, str(err)
        return True, "/output/" + pkgname + '/' + filename

    @classmethod
    def format_time(cls):
        '''
        function:  将当前时间格式化为字符串
        '''
        now_time = str(datetime.datetime.now())
        now_time = now_time.replace(" ", "-").replace(":", "-")
        now_time = now_time.split('.')[0]
        return now_time
#***********************************************************************************
if __name__ == '__main__':
    AdRender()


