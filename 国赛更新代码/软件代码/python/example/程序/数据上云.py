from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from mywindow import *
# -*- coding: cp936 -*-
import ctypes
import os
import time
#import numpy
from ctypes import *
from ctypes import create_string_buffer
from ctypes import c_buffer
from ctypes import sizeof
import time
import uptocloud
import uptocloud as up
Dir_USB2UARTSPIIICDLL = "USB2UARTSPIIICDLL.dll"
print(Dir_USB2UARTSPIIICDLL)
I2cDriver_dll_Usb = ctypes.CDLL(Dir_USB2UARTSPIIICDLL,winmode=0)
Is_Open  = I2cDriver_dll_Usb.OpenUsb(ctypes.c_int(0))
print(Is_Open)
Is_True = I2cDriver_dll_Usb.ConfigIICParam(ctypes.c_uint(0),ctypes.c_uint(10000),ctypes.c_uint(0))
print(Is_True)
print('初始化完成')
def trans(a):
    b= bin(int(a,16))[2:]
    lenth = len(b)
    b = (4-lenth)*'0'+b
    return b
def pre(m):
    w = ['']*4
    re = ['']*2
    n = 0
    x = 0
    for i in m:
        if n == 1:
            w[x] = i
            x += 1
        if i == 'x':
            n = 1
        # if i == 'n':
        #     n = 0
    re[0] = w[0]
    re[1] = w[1]
    if re[1] == '':
        re[1] = '0'
    return re

raddr1 = (c_char * 1)()
raddr2 = (c_char * 1)()
send = (c_char * 1)()
recive = (c_char * 2)()

raddr2 = b"\x00"
recive = b"\x00\x00"
for i in range(1,1000):
    r = I2cDriver_dll_Usb.IICRegisterRead(ctypes.c_bool(0), ctypes.c_uint(0x48), raddr2, recive, ctypes.c_char(1),ctypes.c_uint(2), ctypes.c_uint(0))
    A = ('%#x' % recive[0])
    B = ('%#x' % recive[1])
    result = pre(str(A))
    result1 = trans(result[0]) + trans(result[1])
    result = pre(str(B))
    result2 = trans(result[0]) + trans(result[1])
    temp = result1 + result2[0:3]
    temp = float((int(temp, 2))) * 0.125
    print(temp)
    up.upload(temp)
    time.sleep(0.5)


