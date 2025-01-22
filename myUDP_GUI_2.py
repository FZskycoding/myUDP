import socket
import threading

from PyQt5.QtCore import QTimer

from openpyxl import Workbook
import time

import math


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QMessageBox)
from mplwidget import MplWidget

import pandas as pd
from scipy.signal import butter, filtfilt

import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1260, 970)
        MainWindow.setMinimumSize(QtCore.QSize(1260, 970))
        MainWindow.setMaximumSize(QtCore.QSize(1260, 970))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(-1, 0, 1251, 921))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_leftside = QtWidgets.QVBoxLayout()
        self.verticalLayout_leftside.setObjectName("verticalLayout_leftside")

        #COM_Select
        self.GroupBox_hostIP = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.GroupBox_hostIP.setFont(font)
        self.GroupBox_hostIP.setObjectName("GroupBox_hostIP")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.GroupBox_hostIP)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 241, 71))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_COM_select = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_COM_select.setContentsMargins(0, 0, 10, 0)
        self.verticalLayout_COM_select.setObjectName("verticalLayout_COM_select")

        self.hostIPLayout = QtWidgets.QVBoxLayout()
        self.hostIPLayout.setObjectName("hostIPLayout")
        self.LineEdit_hostIP = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.LineEdit_hostIP.setObjectName("LineEdit_hostIP")
        # self.LineEdit_hostIP.setGeometry(QtCore.QRect(10, 20, 237, 29))
        self.hostIPLayout.addWidget(self.LineEdit_hostIP)
        self.verticalLayout_COM_select.addLayout(self.hostIPLayout)
        

        self.horizontalLayout_COM_Select_btn = QtWidgets.QHBoxLayout()
        self.horizontalLayout_COM_Select_btn.setObjectName("horizontalLayout_COM_Select_btn")
        
        #COM_Select.....連接按鈕&查詢按鈕
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_COM_Select_btn.addItem(spacerItem1)

        self.btn_COMconnect = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.btn_COMconnect.setObjectName("btn_COMconnect")
        self.horizontalLayout_COM_Select_btn.addWidget(self.btn_COMconnect)
        self.btn_IPsearch = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.btn_IPsearch.setObjectName("btn_IPsearch")
        self.horizontalLayout_COM_Select_btn.addWidget(self.btn_IPsearch)


        self.verticalLayout_COM_select.addLayout(self.horizontalLayout_COM_Select_btn)
        self.verticalLayout_COM_select.setStretch(0, 5)
        self.verticalLayout_COM_select.setStretch(1, 5)

        # self.horizontalLayout_COM_Select_btn.setStretch(0, 20)
        # self.horizontalLayout_COM_Select_btn.setStretch(1, 3)
        # self.horizontalLayout_COM_Select_btn.setStretch(2, 1)
        self.horizontalLayout_COM_Select_btn.setContentsMargins(10, 10, 10, 10)
        
        self.verticalLayout_leftside.addWidget(self.GroupBox_hostIP)

        #刀把IP位址
        self.GroupBox_clientIP = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.GroupBox_clientIP.setFont(font)
        self.GroupBox_clientIP.setObjectName("GroupBox_clientIP")
        self.LineEdit_client = QtWidgets.QLineEdit(self.GroupBox_clientIP)
        self.LineEdit_client.setGeometry(QtCore.QRect(10, 20, 237, 29))
        self.LineEdit_client.setObjectName("LineEdit_client")
        self.verticalLayout_leftside.addWidget(self.GroupBox_clientIP)

        #顯示設定
        self.GroupBox_display_Setting = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.GroupBox_display_Setting.setFont(font)
        self.GroupBox_display_Setting.setObjectName("GroupBox_display_Setting")
        self.verticalLayoutWidget_displaySetting = QtWidgets.QWidget(self.GroupBox_display_Setting)
        self.verticalLayoutWidget_displaySetting.setGeometry(QtCore.QRect(10, 20, 221, 161))
        self.verticalLayoutWidget_displaySetting.setObjectName("verticalLayoutWidget_displaySetting")
        self.verticalLayout_displaySetting = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_displaySetting)
        self.verticalLayout_displaySetting.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_displaySetting.setObjectName("verticalLayout_displaySetting")
        # 管理勾選框版面配置
        self.horizontalLayout_ckb_AccAndRms = QtWidgets.QHBoxLayout()
        # 物件之間的空格數
        self.horizontalLayout_ckb_AccAndRms.setSpacing(10)
        self.horizontalLayout_ckb_AccAndRms.setObjectName("horizontalLayout_ckb_AccAndRms")
        self.ckb_acc = QtWidgets.QCheckBox(self.verticalLayoutWidget_displaySetting)
        self.ckb_acc.setObjectName("ckb_acc")
        self.horizontalLayout_ckb_AccAndRms.addWidget(self.ckb_acc)
        self.ckb_acc_out = QtWidgets.QCheckBox(self.verticalLayoutWidget_displaySetting)
        self.ckb_acc_out.setObjectName("ckb_acc_out")
        self.horizontalLayout_ckb_AccAndRms.addWidget(self.ckb_acc_out)
        # ---------------------新增RMS功能--------------------- #
        self.ckb_rms = QtWidgets.QCheckBox(self.verticalLayoutWidget_displaySetting)
        self.ckb_rms.setObjectName("ckb_rms")
        self.horizontalLayout_ckb_AccAndRms.addWidget(self.ckb_rms)
        # ----------------------------------------------------- #
        self.verticalLayout_displaySetting.addLayout(self.horizontalLayout_ckb_AccAndRms)
        self.horizontalLayout_ckb_XYZ = QtWidgets.QHBoxLayout()
        self.horizontalLayout_ckb_XYZ.setObjectName("horizontalLayout_ckb_XYZ")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_ckb_XYZ.addItem(spacerItem2)
        self.verticalLayout_ckb_XYZ = QtWidgets.QVBoxLayout()
        self.verticalLayout_ckb_XYZ.setObjectName("verticalLayout_ckb_XYZ")
        self.ckb_X = QtWidgets.QCheckBox(self.verticalLayoutWidget_displaySetting)
        self.ckb_X.setObjectName("ckb_X")
        self.verticalLayout_ckb_XYZ.addWidget(self.ckb_X)
        self.ckb_Y = QtWidgets.QCheckBox(self.verticalLayoutWidget_displaySetting)
        self.ckb_Y.setObjectName("ckb_Y")
        self.verticalLayout_ckb_XYZ.addWidget(self.ckb_Y)
        self.ckb_Z = QtWidgets.QCheckBox(self.verticalLayoutWidget_displaySetting)
        self.ckb_Z.setObjectName("ckb_Z")
        self.verticalLayout_ckb_XYZ.addWidget(self.ckb_Z)
        self.horizontalLayout_ckb_XYZ.addLayout(self.verticalLayout_ckb_XYZ)
        self.horizontalLayout_ckb_XYZ.setStretch(0, 1)
        self.horizontalLayout_ckb_XYZ.setStretch(1, 9)
        self.verticalLayout_displaySetting.addLayout(self.horizontalLayout_ckb_XYZ)
        self.verticalLayout_displaySetting.setStretch(0, 2)
        self.verticalLayout_displaySetting.setStretch(1, 6)
        self.verticalLayout_leftside.addWidget(self.GroupBox_display_Setting)
        #加速度
        self.groupBox_acceleration = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox_acceleration.setObjectName("groupBox_acceleration")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_acceleration)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 229, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.label_accX = QtWidgets.QLabel(self.layoutWidget)
        self.label_accX.setObjectName("label_accX")
        self.horizontalLayout_8.addWidget(self.label_accX)
        self.line_accX = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_accX.setObjectName("line_accX")
        self.horizontalLayout_8.addWidget(self.line_accX)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.label_accY = QtWidgets.QLabel(self.layoutWidget)
        self.label_accY.setObjectName("label_accY")
        self.horizontalLayout_7.addWidget(self.label_accY)
        self.line_accY = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_accY.setObjectName("line_accY")
        self.horizontalLayout_7.addWidget(self.line_accY)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.label_accZ = QtWidgets.QLabel(self.layoutWidget)
        self.label_accZ.setObjectName("label_accZ")
        self.horizontalLayout_9.addWidget(self.label_accZ)
        self.line_accZ = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_accZ.setObjectName("line_accZ")
        self.horizontalLayout_9.addWidget(self.line_accZ)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout_7.setStretch(0, 2)
        self.verticalLayout_7.setStretch(1, 2)
        self.verticalLayout_7.setStretch(2, 2)
        self.verticalLayout_leftside.addWidget(self.groupBox_acceleration)
        #新增最大最小值
        #------------------------ckb_X的最大最小--------------------------#
        self.horizontalLayout_display_settingX = QtWidgets.QHBoxLayout()
        self.horizontalLayout_display_settingX.addWidget(self.ckb_X)
        self.horizontalLayout_display_settingX.setObjectName("horizontalLayout_display_settingX")
        self.verticalLayout_ckb_XYZ.addLayout(self.horizontalLayout_display_settingX)

        self.lineEdit_Xmin = QtWidgets.QLineEdit(self.verticalLayoutWidget_displaySetting)
        self.lineEdit_Xmin.setObjectName("lineEdit_Xmin")
        self.horizontalLayout_display_settingX.addWidget(self.lineEdit_Xmin)

        self.label_XminTomax = QtWidgets.QLabel(self.verticalLayoutWidget_displaySetting)
        self.label_XminTomax.setObjectName("label_XminTomax")
        self.horizontalLayout_display_settingX.addWidget(self.label_XminTomax)

        self.lineEdit_Xmax = QtWidgets.QLineEdit(self.verticalLayoutWidget_displaySetting)
        self.lineEdit_Xmax.setObjectName("lineEdit_Xmax")
        self.horizontalLayout_display_settingX.addWidget(self.lineEdit_Xmax)
       
        #------------------------ckb_Y的最大最小--------------------------#
        self.horizontalLayout_display_settingY = QtWidgets.QHBoxLayout()
        self.horizontalLayout_display_settingY.addWidget(self.ckb_Y)
        self.horizontalLayout_display_settingY.setObjectName("horizontalLayout_display_settingY")
        self.verticalLayout_ckb_XYZ.addLayout(self.horizontalLayout_display_settingY)

        self.lineEdit_Ymin = QtWidgets.QLineEdit(self.verticalLayoutWidget_displaySetting)
        self.lineEdit_Ymin.setObjectName("lineEdit_Ymin")
        self.horizontalLayout_display_settingY.addWidget(self.lineEdit_Ymin)

        self.label_YminTomax = QtWidgets.QLabel(self.verticalLayoutWidget_displaySetting)
        self.label_YminTomax.setObjectName("label_YminTomax")
        self.horizontalLayout_display_settingY.addWidget(self.label_YminTomax)

        self.lineEdit_Ymax = QtWidgets.QLineEdit(self.verticalLayoutWidget_displaySetting)
        self.lineEdit_Ymax.setObjectName("lineEdit_Ymax")
        self.horizontalLayout_display_settingY.addWidget(self.lineEdit_Ymax)        
        
        #------------------------ckb_Z的最大最小--------------------------#
        self.horizontalLayout_display_settingZ = QtWidgets.QHBoxLayout()
        self.horizontalLayout_display_settingZ.addWidget(self.ckb_Z)
        self.horizontalLayout_display_settingZ.setObjectName("horizontalLayout_display_settingZ")
        self.verticalLayout_ckb_XYZ.addLayout(self.horizontalLayout_display_settingZ)

        self.lineEdit_Zmin = QtWidgets.QLineEdit(self.verticalLayoutWidget_displaySetting)
        self.lineEdit_Zmin.setObjectName("lineEdit_Zmin")
        self.horizontalLayout_display_settingZ.addWidget(self.lineEdit_Zmin)

        self.label_ZminTomax = QtWidgets.QLabel(self.verticalLayoutWidget_displaySetting)
        self.label_ZminTomax.setObjectName("label_ZminTomax")
        self.horizontalLayout_display_settingZ.addWidget(self.label_ZminTomax)

        self.lineEdit_Zmax = QtWidgets.QLineEdit(self.verticalLayoutWidget_displaySetting)
        self.lineEdit_Zmax.setObjectName("lineEdit_Zmax")
        self.horizontalLayout_display_settingZ.addWidget(self.lineEdit_Zmax)
        #加速度模式
        self.ComboBox_accMode = QtWidgets.QComboBox(self.verticalLayoutWidget_displaySetting)   # 加入下拉選單
        self.ComboBox_accMode.addItems(['8G','16G','32G','64G'])   # 加入四個選項
        self.ComboBox_accMode.setCurrentText('64G') 
        self.verticalLayout_ckb_XYZ.addWidget(self.ComboBox_accMode)
        # self.ckb_8G = QtWidgets.QCheckBox(self.verticalLayoutWidget_displaySetting)
        # self.ckb_8G.setObjectName("ckb_8G")
        # self.verticalLayout_ckb_XYZ.addWidget(self.ckb_8G)
  
        #確認按鈕
        self.btn_displaySetting_confirm = QtWidgets.QPushButton(self.GroupBox_display_Setting)
        self.btn_displaySetting_confirm.setGeometry(QtCore.QRect(155, 180, 75, 23))
        self.btn_displaySetting_confirm.setObjectName("btn_displaySetting_confirm")
        #顯示取樣率
        self.horizontalLayout_display_setting_frequency = QtWidgets.QHBoxLayout()
        self.label_frequency = QtWidgets.QLabel(self.verticalLayoutWidget_displaySetting)
        self.label_frequency.setObjectName("label_frequency")
        self.horizontalLayout_display_setting_frequency.addWidget(self.label_frequency)
        # self.label_frequency.setText("取樣率 : ")
        self.verticalLayout_ckb_XYZ.addLayout(self.horizontalLayout_display_setting_frequency)

        #設置
        self.groupBox_setting = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox_setting.setObjectName("groupBox_setting")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_setting)
        
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 229, 171))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_setting = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_setting.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_setting.setObjectName("verticalLayout_setting")

        #lowcut
        self.horizontalLayout_lowcut = QtWidgets.QHBoxLayout()
        self.horizontalLayout_lowcut.setObjectName("horizontalLayout_lowcut")
        spacerItem_lowcut = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_lowcut.addItem(spacerItem_lowcut)
        self.label_lowcut = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_lowcut.setObjectName("label_lowcut")
        self.horizontalLayout_lowcut.addWidget(self.label_lowcut)
        self.lineEdit_lowcut = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_lowcut.setObjectName("lineEdit_lowcut")
        self.horizontalLayout_lowcut.addWidget(self.lineEdit_lowcut) 

        self.horizontalLayout_lowcut.setStretch(0, 1)
        self.horizontalLayout_lowcut.setStretch(1, 1)
        self.horizontalLayout_lowcut.setStretch(2, 7)
        self.verticalLayout_setting.addLayout(self.horizontalLayout_lowcut)

        #highcut
        self.horizontalLayout_highcut = QtWidgets.QHBoxLayout()
        self.horizontalLayout_highcut.setObjectName("horizontalLayout_highcut")
        spacerItem_highcut = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_highcut.addItem(spacerItem_highcut)
        self.label_highcut = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_highcut.setObjectName("label_highcut")
        self.horizontalLayout_highcut.addWidget(self.label_highcut)
        self.lineEdit_highcut = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_highcut.setObjectName("lineEdit_highcut")
        self.horizontalLayout_highcut.addWidget(self.lineEdit_highcut)
        self.horizontalLayout_highcut.setStretch(0, 1)
        self.horizontalLayout_highcut.setStretch(1, 1)
        self.horizontalLayout_highcut.setStretch(2, 7)
        self.verticalLayout_setting.addLayout(self.horizontalLayout_highcut)

        # 電量
        self.horizontalLayout_power = QtWidgets.QHBoxLayout()
        self.horizontalLayout_power.setObjectName("horizontalLayout_power")
        
        self.label_power = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_power.setObjectName("label_power")
        self.horizontalLayout_power.addWidget(self.label_power)
        self.value_power = QtWidgets.QLabel(self.layoutWidget_2)
        self.value_power.setObjectName("value_power")
        self.horizontalLayout_power.addWidget(self.value_power)
        self.horizontalLayout_power.setStretch(0, 1)
        self.horizontalLayout_power.setStretch(1, 2)
        self.verticalLayout_setting.addLayout(self.horizontalLayout_power)

        # 電壓
        self.horizontalLayout_voltage = QtWidgets.QHBoxLayout()
        self.horizontalLayout_voltage.setObjectName("horizontalLayout_voltage")
        self.label_voltage = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_voltage.setObjectName("label_voltage")
        self.horizontalLayout_voltage.addWidget(self.label_voltage)
        self.value_voltage = QtWidgets.QLabel(self.layoutWidget_2)
        self.value_voltage.setObjectName("value_voltage")
        self.horizontalLayout_voltage.addWidget(self.value_voltage)
        self.horizontalLayout_voltage.setStretch(0, 1)
        self.horizontalLayout_voltage.setStretch(1, 2)
        self.verticalLayout_setting.addLayout(self.horizontalLayout_voltage)

        # 電流
        self.horizontalLayout_current = QtWidgets.QHBoxLayout()
        self.horizontalLayout_current.setObjectName("horizontalLayout_current")
        self.label_current = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_current.setObjectName("label_current")
        self.horizontalLayout_current.addWidget(self.label_current)
        self.value_current = QtWidgets.QLabel(self.layoutWidget_2)
        self.value_current.setObjectName("value_current")
        self.horizontalLayout_current.addWidget(self.value_current)
        self.horizontalLayout_current.setStretch(0, 1)
        self.horizontalLayout_current.setStretch(1, 2)
        self.verticalLayout_setting.addLayout(self.horizontalLayout_current)
        
        

        #調整設置區塊物件的垂直分布
        self.verticalLayout_setting.setStretch(0, 1)
        self.verticalLayout_setting.setStretch(1, 1)
        self.verticalLayout_setting.setStretch(2, 1)
        self.verticalLayout_setting.setStretch(3, 1)
        self.verticalLayout_setting.setStretch(4, 1)
        
        self.verticalLayout_leftside.addWidget(self.groupBox_setting)
        self.verticalLayout_leftside.setStretch(0, 1)
        self.verticalLayout_leftside.setStretch(1, 1)
        self.verticalLayout_leftside.setStretch(2, 2)
        self.verticalLayout_leftside.setStretch(3, 2)
        self.verticalLayout_leftside.setStretch(4, 2)
        self.horizontalLayout_19.addLayout(self.verticalLayout_leftside)

        #顯示
        self.groupBox_display = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.groupBox_display.setFont(font)
        self.groupBox_display.setObjectName("groupBox_display")
        self.display_widget = QtWidgets.QWidget(self.groupBox_display)
        self.display_widget.setGeometry(QtCore.QRect(10, 20, 981, 891))
        self.display_widget.setObjectName("display_widget")
        self.display_verticalLayout = QtWidgets.QVBoxLayout(self.display_widget)
        self.display_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.display_verticalLayout.setObjectName("display_verticalLayout")

        self.MplWidget = MplWidget(self.display_widget)
        self.MplWidget.setObjectName("MplWidget")
        self.display_verticalLayout.addWidget(self.MplWidget)

        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.btn_record = QtWidgets.QPushButton(self.display_widget)
        self.btn_record.setObjectName("btn_record")
        self.horizontalLayout_18.addWidget(self.btn_record)
        self.btn_save = QtWidgets.QPushButton(self.display_widget)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_18.addWidget(self.btn_save)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem8)


        self.btn_stop = QtWidgets.QPushButton(self.display_widget)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_18.addWidget(self.btn_stop)
        self.display_verticalLayout.addLayout(self.horizontalLayout_18)

        self.display_verticalLayout.setStretch(0, 18)
        self.display_verticalLayout.setStretch(1, 1)
        self.horizontalLayout_19.addWidget(self.groupBox_display)
        self.horizontalLayout_19.setStretch(0, 2)
        self.horizontalLayout_19.setStretch(1, 8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1260, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GroupBox_hostIP.setTitle(_translate("MainWindow", "COM Select"))
        self.LineEdit_hostIP.setText(_translate("MainWindow", "0.0.0.0"))
        self.btn_IPsearch.setText(_translate("MainWindow", "查詢"))
        self.btn_COMconnect.setText(_translate("MainWindow", "連接"))
        self.GroupBox_clientIP.setTitle(_translate("MainWindow", "刀把IP地址"))
        self.LineEdit_client.setText(_translate("MainWindow", "0.0.0.0"))
        self.GroupBox_display_Setting.setTitle(_translate("MainWindow", "顯示設定"))
        self.ckb_acc.setText(_translate("MainWindow", "加速度"))
        self.ckb_acc_out.setText(_translate("MainWindow", "加速度(濾波)"))
        self.ckb_rms.setText(_translate("MainWindow", "RMS"))
        self.ckb_X.setText(_translate("MainWindow", "X"))
        self.ckb_Y.setText(_translate("MainWindow", "Y"))
        self.ckb_Z.setText(_translate("MainWindow", "Z"))

        # self.ckb_8G.setText(_translate("MainWindow", "8G"))

        self.groupBox_acceleration.setTitle(_translate("MainWindow", "加速度:"))
        self.label_accX.setText(_translate("MainWindow", "X:"))
        self.label_accY.setText(_translate("MainWindow", "Y:"))
        self.label_accZ.setText(_translate("MainWindow", "Z:"))
        self.groupBox_setting.setTitle(_translate("MainWindow", "設置:"))
        self.label_lowcut.setText(_translate("MainWindow", "lowcut:"))
        self.label_highcut.setText(_translate("MainWindow", "highcut:"))
        self.label_power.setText(_translate("MainWindow", "電量:"))
        self.value_power.setText(_translate("MainWindow", "N/A"))
        self.label_voltage.setText(_translate("MainWindow", "電壓:"))
        self.value_voltage.setText(_translate("MainWindow", "N/A"))
        self.label_current.setText(_translate("MainWindow", "電流:"))
        self.value_current.setText(_translate("MainWindow", "N/A"))
        self.groupBox_display.setTitle(_translate("MainWindow", "顯示"))
        self.btn_record.setText(_translate("MainWindow", "紀錄"))
        self.btn_save.setText(_translate("MainWindow", "保存"))
        self.btn_stop.setText(_translate("MainWindow", "暫停"))

        #新增min_max功能
        #------------------------X------------------------#
        self.lineEdit_Xmin.setPlaceholderText(_translate("MainWindow", "min"))
        self.label_XminTomax.setText(_translate("MainWindow", "~"))
        self.lineEdit_Xmax.setPlaceholderText(_translate("MainWindow", "max"))
        #------------------------Y------------------------#
        self.lineEdit_Ymin.setPlaceholderText(_translate("MainWindow", "min"))
        self.label_YminTomax.setText(_translate("MainWindow", "~"))
        self.lineEdit_Ymax.setPlaceholderText(_translate("MainWindow", "max"))
        #------------------------Z------------------------#
        self.lineEdit_Zmin.setPlaceholderText(_translate("MainWindow", "min"))
        self.label_ZminTomax.setText(_translate("MainWindow", "~"))
        self.lineEdit_Zmax.setPlaceholderText(_translate("MainWindow", "max"))

        #---------------------確認按鈕---------------------#
        self.btn_displaySetting_confirm.setText(_translate("MainWindow", "確認"))
