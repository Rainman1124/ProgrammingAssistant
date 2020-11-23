# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\wf_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 572)
        MainWindow.setStyleSheet("QPushButton{\n"
"    font: 75 10pt \"微软雅黑\";\n"
"    background-color: rgba(0, 0, 74, 200);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    border:1px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    font: 75 10pt \"微软雅黑\";\n"
"    background-color: rgba(85, 255, 255,200);\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border:1px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    font: 75 10pt \"微软雅黑\";\n"
"    background-color: rgba(255, 0, 0,200);\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border:1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#bt_dm,#bt_python,#bt_spider,#bt_pyQt5,#bt_lw,#bt_win32,#bt_webkj,#bt_gb{\n"
"    font: 75 10pt \"微软雅黑\";\n"
"    background-color: rgba(0, 0, 0,200);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    border:1px solid rgb(255, 255, 255);\n"
"}\n"
"#bt_dm:hover,#bt_python:hover,#bt_spider:hover,#bt_pyQt5:hover,#bt_lw:hover,#bt_win32:hover,#bt_webkj:hover,#bt_gb:hover{\n"
"    font: 75 10pt \"微软雅黑\";\n"
"    background-color: rgba(85, 255, 255,200);\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border:1px solid rgb(255, 255, 255);\n"
"}\n"
"#bt_dm:pressed,#bt_python:pressed,#bt_spider:pressed,#bt_pyQt5:pressed,#bt_lw:pressed,#bt_win32:pressed,#bt_webkj:pressed,#bt_gb:pressed{\n"
"    font: 75 10pt \"微软雅黑\";\n"
"    background-color: rgba(255, 0, 0,200);\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border:1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_python = QtWidgets.QFrame(self.centralwidget)
        self.frame_python.setGeometry(QtCore.QRect(70, 0, 291, 71))
        self.frame_python.setObjectName("frame_python")
        self.frame_python_hb = QtWidgets.QHBoxLayout(self.frame_python)
        self.frame_python_hb.setContentsMargins(0, 0, 0, 0)
        self.frame_python_hb.setSpacing(0)
        self.frame_python_hb.setObjectName("frame_python_hb")
        self.bt_python_ksrm = QtWidgets.QPushButton(self.frame_python)
        self.bt_python_ksrm.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_python_ksrm.setObjectName("bt_python_ksrm")
        self.frame_python_hb.addWidget(self.bt_python_ksrm)
        self.bt_python_scbd = QtWidgets.QPushButton(self.frame_python)
        self.bt_python_scbd.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_python_scbd.setObjectName("bt_python_scbd")
        self.frame_python_hb.addWidget(self.bt_python_scbd)
        self.bt_python_gnhs = QtWidgets.QPushButton(self.frame_python)
        self.bt_python_gnhs.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_python_gnhs.setObjectName("bt_python_gnhs")
        self.frame_python_hb.addWidget(self.bt_python_gnhs)
        self.bt_python_lrgj = QtWidgets.QPushButton(self.frame_python)
        self.bt_python_lrgj.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_python_lrgj.setObjectName("bt_python_lrgj")
        self.frame_python_hb.addWidget(self.bt_python_lrgj)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frame_python_hb.addItem(spacerItem)
        self.frame_spider = QtWidgets.QFrame(self.centralwidget)
        self.frame_spider.setGeometry(QtCore.QRect(70, 70, 291, 71))
        self.frame_spider.setObjectName("frame_spider")
        self.frame_spider_hb = QtWidgets.QHBoxLayout(self.frame_spider)
        self.frame_spider_hb.setContentsMargins(0, 0, 0, 0)
        self.frame_spider_hb.setSpacing(0)
        self.frame_spider_hb.setObjectName("frame_spider_hb")
        self.bt_spider_ksrm = QtWidgets.QPushButton(self.frame_spider)
        self.bt_spider_ksrm.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_spider_ksrm.setObjectName("bt_spider_ksrm")
        self.frame_spider_hb.addWidget(self.bt_spider_ksrm)
        self.bt_spider_scbd = QtWidgets.QPushButton(self.frame_spider)
        self.bt_spider_scbd.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_spider_scbd.setObjectName("bt_spider_scbd")
        self.frame_spider_hb.addWidget(self.bt_spider_scbd)
        self.bt_spider_zbgj = QtWidgets.QPushButton(self.frame_spider)
        self.bt_spider_zbgj.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_spider_zbgj.setObjectName("bt_spider_zbgj")
        self.frame_spider_hb.addWidget(self.bt_spider_zbgj)
        self.bt_spider_jsonjx = QtWidgets.QPushButton(self.frame_spider)
        self.bt_spider_jsonjx.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_spider_jsonjx.setObjectName("bt_spider_jsonjx")
        self.frame_spider_hb.addWidget(self.bt_spider_jsonjx)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frame_spider_hb.addItem(spacerItem1)
        self.frame_pyQt5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_pyQt5.setGeometry(QtCore.QRect(70, 140, 291, 71))
        self.frame_pyQt5.setObjectName("frame_pyQt5")
        self.frame_pyqt5_hb = QtWidgets.QHBoxLayout(self.frame_pyQt5)
        self.frame_pyqt5_hb.setContentsMargins(0, 0, 0, 0)
        self.frame_pyqt5_hb.setSpacing(0)
        self.frame_pyqt5_hb.setObjectName("frame_pyqt5_hb")
        self.bt_pyQt5_ksrm = QtWidgets.QPushButton(self.frame_pyQt5)
        self.bt_pyQt5_ksrm.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_pyQt5_ksrm.setObjectName("bt_pyQt5_ksrm")
        self.frame_pyqt5_hb.addWidget(self.bt_pyQt5_ksrm)
        self.bt_pyQt5_scbd = QtWidgets.QPushButton(self.frame_pyQt5)
        self.bt_pyQt5_scbd.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_pyQt5_scbd.setObjectName("bt_pyQt5_scbd")
        self.frame_pyqt5_hb.addWidget(self.bt_pyQt5_scbd)
        self.bt_pyQt5_qssbd = QtWidgets.QPushButton(self.frame_pyQt5)
        self.bt_pyQt5_qssbd.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_pyQt5_qssbd.setObjectName("bt_pyQt5_qssbd")
        self.frame_pyqt5_hb.addWidget(self.bt_pyQt5_qssbd)
        self.bt_pyQt5_qssgj = QtWidgets.QPushButton(self.frame_pyQt5)
        self.bt_pyQt5_qssgj.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_pyQt5_qssgj.setObjectName("bt_pyQt5_qssgj")
        self.frame_pyqt5_hb.addWidget(self.bt_pyQt5_qssgj)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frame_pyqt5_hb.addItem(spacerItem2)
        self.frame_dm = QtWidgets.QFrame(self.centralwidget)
        self.frame_dm.setGeometry(QtCore.QRect(70, 210, 291, 71))
        self.frame_dm.setObjectName("frame_dm")
        self.frame_dm_hb = QtWidgets.QHBoxLayout(self.frame_dm)
        self.frame_dm_hb.setContentsMargins(0, 0, 0, 0)
        self.frame_dm_hb.setSpacing(0)
        self.frame_dm_hb.setObjectName("frame_dm_hb")
        self.bt_dm_ksrm = QtWidgets.QPushButton(self.frame_dm)
        self.bt_dm_ksrm.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_dm_ksrm.setObjectName("bt_dm_ksrm")
        self.frame_dm_hb.addWidget(self.bt_dm_ksrm)
        self.bt_dm_scbd = QtWidgets.QPushButton(self.frame_dm)
        self.bt_dm_scbd.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_dm_scbd.setObjectName("bt_dm_scbd")
        self.frame_dm_hb.addWidget(self.bt_dm_scbd)
        self.bt_dm_zhgj = QtWidgets.QPushButton(self.frame_dm)
        self.bt_dm_zhgj.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_dm_zhgj.setObjectName("bt_dm_zhgj")
        self.frame_dm_hb.addWidget(self.bt_dm_zhgj)
        self.bt_dm_bdgj = QtWidgets.QPushButton(self.frame_dm)
        self.bt_dm_bdgj.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_dm_bdgj.setObjectName("bt_dm_bdgj")
        self.frame_dm_hb.addWidget(self.bt_dm_bdgj)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frame_dm_hb.addItem(spacerItem3)
        self.frame_lw = QtWidgets.QFrame(self.centralwidget)
        self.frame_lw.setGeometry(QtCore.QRect(70, 280, 291, 71))
        self.frame_lw.setObjectName("frame_lw")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_lw)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bt_lw_ksrm = QtWidgets.QPushButton(self.frame_lw)
        self.bt_lw_ksrm.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_lw_ksrm.setObjectName("bt_lw_ksrm")
        self.horizontalLayout_5.addWidget(self.bt_lw_ksrm)
        self.bt_lw_scbd = QtWidgets.QPushButton(self.frame_lw)
        self.bt_lw_scbd.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_lw_scbd.setObjectName("bt_lw_scbd")
        self.horizontalLayout_5.addWidget(self.bt_lw_scbd)
        self.bt_lw_lwzs = QtWidgets.QPushButton(self.frame_lw)
        self.bt_lw_lwzs.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_lw_lwzs.setObjectName("bt_lw_lwzs")
        self.horizontalLayout_5.addWidget(self.bt_lw_lwzs)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.frame_win32 = QtWidgets.QFrame(self.centralwidget)
        self.frame_win32.setGeometry(QtCore.QRect(70, 350, 291, 71))
        self.frame_win32.setObjectName("frame_win32")
        self.frame_win32_hb = QtWidgets.QHBoxLayout(self.frame_win32)
        self.frame_win32_hb.setContentsMargins(0, 0, 0, 0)
        self.frame_win32_hb.setSpacing(0)
        self.frame_win32_hb.setObjectName("frame_win32_hb")
        self.bt_win32_ksrm = QtWidgets.QPushButton(self.frame_win32)
        self.bt_win32_ksrm.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_win32_ksrm.setObjectName("bt_win32_ksrm")
        self.frame_win32_hb.addWidget(self.bt_win32_ksrm)
        self.bt_win32_scbd = QtWidgets.QPushButton(self.frame_win32)
        self.bt_win32_scbd.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_win32_scbd.setObjectName("bt_win32_scbd")
        self.frame_win32_hb.addWidget(self.bt_win32_scbd)
        self.bt_win32_apizs = QtWidgets.QPushButton(self.frame_win32)
        self.bt_win32_apizs.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_win32_apizs.setObjectName("bt_win32_apizs")
        self.frame_win32_hb.addWidget(self.bt_win32_apizs)
        self.bt_win32_jyzs = QtWidgets.QPushButton(self.frame_win32)
        self.bt_win32_jyzs.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_win32_jyzs.setObjectName("bt_win32_jyzs")
        self.frame_win32_hb.addWidget(self.bt_win32_jyzs)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frame_win32_hb.addItem(spacerItem5)
        self.frame_webkj = QtWidgets.QFrame(self.centralwidget)
        self.frame_webkj.setGeometry(QtCore.QRect(70, 420, 291, 71))
        self.frame_webkj.setObjectName("frame_webkj")
        self.flask_hb = QtWidgets.QHBoxLayout(self.frame_webkj)
        self.flask_hb.setContentsMargins(0, 0, 0, 0)
        self.flask_hb.setSpacing(0)
        self.flask_hb.setObjectName("flask_hb")
        self.bt_webkj_ksrm = QtWidgets.QPushButton(self.frame_webkj)
        self.bt_webkj_ksrm.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_webkj_ksrm.setObjectName("bt_webkj_ksrm")
        self.flask_hb.addWidget(self.bt_webkj_ksrm)
        self.bt_webkj_scbd = QtWidgets.QPushButton(self.frame_webkj)
        self.bt_webkj_scbd.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_webkj_scbd.setObjectName("bt_webkj_scbd")
        self.flask_hb.addWidget(self.bt_webkj_scbd)
        self.bt_webkj_lrgj = QtWidgets.QPushButton(self.frame_webkj)
        self.bt_webkj_lrgj.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_webkj_lrgj.setObjectName("bt_webkj_lrgj")
        self.flask_hb.addWidget(self.bt_webkj_lrgj)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.flask_hb.addItem(spacerItem6)
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setGeometry(QtCore.QRect(0, 0, 73, 511))
        self.frame_main.setObjectName("frame_main")
        self.frame_main_hb = QtWidgets.QVBoxLayout(self.frame_main)
        self.frame_main_hb.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.frame_main_hb.setContentsMargins(0, 0, 0, 0)
        self.frame_main_hb.setSpacing(0)
        self.frame_main_hb.setObjectName("frame_main_hb")
        self.bt_python = QtWidgets.QPushButton(self.frame_main)
        self.bt_python.setMinimumSize(QtCore.QSize(71, 71))
        self.bt_python.setObjectName("bt_python")
        self.frame_main_hb.addWidget(self.bt_python)
        self.bt_spider = QtWidgets.QPushButton(self.frame_main)
        self.bt_spider.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_spider.setObjectName("bt_spider")
        self.frame_main_hb.addWidget(self.bt_spider)
        self.bt_pyQt5 = QtWidgets.QPushButton(self.frame_main)
        self.bt_pyQt5.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_pyQt5.setObjectName("bt_pyQt5")
        self.frame_main_hb.addWidget(self.bt_pyQt5)
        self.bt_dm = QtWidgets.QPushButton(self.frame_main)
        self.bt_dm.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_dm.setObjectName("bt_dm")
        self.frame_main_hb.addWidget(self.bt_dm)
        self.bt_lw = QtWidgets.QPushButton(self.frame_main)
        self.bt_lw.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_lw.setObjectName("bt_lw")
        self.frame_main_hb.addWidget(self.bt_lw)
        self.bt_win32 = QtWidgets.QPushButton(self.frame_main)
        self.bt_win32.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_win32.setObjectName("bt_win32")
        self.frame_main_hb.addWidget(self.bt_win32)
        self.bt_webkj = QtWidgets.QPushButton(self.frame_main)
        self.bt_webkj.setMinimumSize(QtCore.QSize(71, 70))
        self.bt_webkj.setObjectName("bt_webkj")
        self.frame_main_hb.addWidget(self.bt_webkj)
        self.bt_gb = QtWidgets.QPushButton(self.frame_main)
        self.bt_gb.setObjectName("bt_gb")
        self.frame_main_hb.addWidget(self.bt_gb)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.bt_gb.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_python_ksrm.setText(_translate("MainWindow", "快速入门"))
        self.bt_python_scbd.setText(_translate("MainWindow", "速查宝典"))
        self.bt_python_gnhs.setText(_translate("MainWindow", "功能函数"))
        self.bt_python_lrgj.setText(_translate("MainWindow", "懒人工具"))
        self.bt_spider_ksrm.setText(_translate("MainWindow", "快速入门"))
        self.bt_spider_scbd.setText(_translate("MainWindow", "速查宝典"))
        self.bt_spider_zbgj.setText(_translate("MainWindow", "抓包工具"))
        self.bt_spider_jsonjx.setText(_translate("MainWindow", "JSON解析"))
        self.bt_pyQt5_ksrm.setText(_translate("MainWindow", "快速入门"))
        self.bt_pyQt5_scbd.setText(_translate("MainWindow", "速查宝典"))
        self.bt_pyQt5_qssbd.setText(_translate("MainWindow", "QSS宝典"))
        self.bt_pyQt5_qssgj.setText(_translate("MainWindow", "QSS工具"))
        self.bt_dm_ksrm.setText(_translate("MainWindow", "快速入门"))
        self.bt_dm_scbd.setText(_translate("MainWindow", "速查宝典"))
        self.bt_dm_zhgj.setText(_translate("MainWindow", "综合工具"))
        self.bt_dm_bdgj.setText(_translate("MainWindow", "绑定工具"))
        self.bt_lw_ksrm.setText(_translate("MainWindow", "快速入门"))
        self.bt_lw_scbd.setText(_translate("MainWindow", "速查宝典"))
        self.bt_lw_lwzs.setText(_translate("MainWindow", "乐玩助手"))
        self.bt_win32_ksrm.setText(_translate("MainWindow", "快速入门"))
        self.bt_win32_scbd.setText(_translate("MainWindow", "速查宝典"))
        self.bt_win32_apizs.setText(_translate("MainWindow", "API易助手"))
        self.bt_win32_jyzs.setText(_translate("MainWindow", "精易助手"))
        self.bt_webkj_ksrm.setText(_translate("MainWindow", "快速入门"))
        self.bt_webkj_scbd.setText(_translate("MainWindow", "速查宝典"))
        self.bt_webkj_lrgj.setText(_translate("MainWindow", "懒人工具"))
        self.bt_python.setText(_translate("MainWindow", "python"))
        self.bt_spider.setText(_translate("MainWindow", "爬虫"))
        self.bt_pyQt5.setToolTip(_translate("MainWindow", "<html><head/><body><p>&lt;h1&gt;python&lt;h1&gt;</p><p>&lt;span&gt;dsgsdgsdg&lt;/span&gt;</p></body></html>"))
        self.bt_pyQt5.setText(_translate("MainWindow", "PyQt5"))
        self.bt_dm.setText(_translate("MainWindow", "大漠"))
        self.bt_lw.setText(_translate("MainWindow", "乐玩"))
        self.bt_win32.setText(_translate("MainWindow", "win32"))
        self.bt_webkj.setText(_translate("MainWindow", "web框架"))
        self.bt_gb.setText(_translate("MainWindow", "关闭"))
