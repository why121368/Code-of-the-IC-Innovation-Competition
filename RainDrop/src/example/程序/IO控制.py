# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:56:01 2023

@author: jackscl
"""

import matplotlib.pyplot as plt
import numpy as np
import time
import sys, os
import pathlib

py_path, py_name = os.path.split(os.path.abspath(__file__))

base_dir = pathlib.Path(py_path).absolute().parent  # sys.argv[0]

if sys.path.count(base_dir) == 0:
    sys.path.append(str(base_dir))

from pyRD import RD
from pyRD.core.RDconstant import *

rd = RD()
rd.DeviceEnumLists()
print(rd.devicelist)
print(rd.DeviceOpen(0))
# Supplies
CHs_OUT = 0x11  # DIO0 enable output
CHs_OUTValue = 0x01  # DIO0 output value set high

for i in range(0,7):
    CHs_OUTValue += 1
    print(CHs_OUTValue)
# rd.DigitalIOOutputEnableSet(CHs_OUT)
# rd.DigitalIOOutputSet(CHs_OUTValue)
# rd.DigitalIOInputStatus()  # first reading drop
#
# time.sleep(0.1)
# j = 10
# while (j > 0):
#     rd.DigitalIOInputStatus()
#     value = rd.stiodata.value
#     print(value)
#     status = []
#     for i in range(16):
#         status.append((value >> i) & 1)
#     print(status)
#     j = j - 1
#     time.sleep(0.1)
# # close connect
# print(rd.DeviceClose())
        self.widget.setGaugeTheme(7)
        self.widget.units = "mA"
        self.widget_2.setGaugeTheme(8)
        self.widget_2.maxValue = 100
        self.widget_3.setGaugeTheme(8)
        self.widget_3.maxValue = 100


        self.progressBar_1.setRange(0, 200)
        self.progressBar_2.setRange(0, 200)
        self.progressBar_3.setRange(0, 200)
        self.progressBar_4.setRange(0, 200)
        self.progressBar_5.setRange(0, 200)
        self.progressBar_6.setRange(0, 200)
        self.progressBar_7.setRange(0, 200)
        self.progressBar_8.setRange(0, 200)
        self.progressBar_9.setRange(0, 200)
        self.progressBar_10.setRange(0, 200)
        self.progressBar_111.setRange(0, 200)

        now_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.lineEdit_12.setText('192.168.137.103')
        self.time.setText(str(now_date))
from analoggaugewidget import AnalogGaugeWidget
