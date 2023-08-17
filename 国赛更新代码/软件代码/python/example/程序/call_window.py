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
import  uptocloud as up
import sms as sms
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
#发送数据
# raddr1 = (c_char * 1)()
# raddr2 = (c_char * 1)()
# send = (c_char * 1)()
# recive = (c_char * 2)()
#
# raddr2 = b"\x00"
# recive= b"\x00\x00"
# for i in range(0,100):
#     r = I2cDriver_dll_Usb.IICRegisterRead(ctypes.c_bool(0),ctypes.c_uint(0x48),raddr2,recive,ctypes.c_char(1),ctypes.c_uint(2),ctypes.c_uint(0))
#     print('%#x'%recive[0])
#     print('%#x'%recive[1])
#     A = ('%#x'%recive[0])
#     B = ('%#x'%recive[1])
#     result = pre(str(A))
#     result1 = trans(result[0]) + trans(result[1])
#     result = pre(str(B))
#     result2 = trans(result[0]) + trans(result[1])
#     temp = result1 + result2[0:3]
#     print(temp)
#     print(int(temp,2))
#     temp = float((int(temp,2)))*0.125
#     print(temp)
#     time.sleep(1)






ret = 1


class MyMainWin(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWin,self).__init__(parent)
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.update_plot_data)
        self.pushButton.clicked.connect(self.start)
        # super(MainWindow, self).__init__(*args, **kwargs)
        # self.graphWidget = pg.PlotWidget()
        # self.setCentralWidget(self.graphWidget)
        self.x = list(range(100))  # 100 time points
        self.y = [randint(25,26) for _ in range(100)]  # 100 data points

        self.widget.setBackground('k')
        self.widget.setBackground('k')
        self.widget.setYRange(25,35 )
        self.widget.showGrid(x=True, y=True)
        pen = pg.mkPen(color=(255, 255, 255))
        self.data_line =  self.widget.plot(self.x, self.y, pen=pen)

    #更新电池状态函数
    def start(self):
        self.timer.start()

    def update_plot_data(self):
        raddr1 = (c_char * 1)()
        raddr2 = (c_char * 1)()
        send = (c_char * 1)()
        recive = (c_char * 2)()

        raddr2 = b"\x00"
        recive = b"\x00\x00"
        r = I2cDriver_dll_Usb.IICRegisterRead(ctypes.c_bool(0), ctypes.c_uint(0x48), raddr2, recive, ctypes.c_char(1),ctypes.c_uint(2), ctypes.c_uint(0))
        A = ('%#x' % recive[0])
        B = ('%#x' % recive[1])
        result = pre(str(A))
        result1 = trans(result[0]) + trans(result[1])
        result = pre(str(B))
        result2 = trans(result[0]) + trans(result[1])
        temp = result1 + result2[0:3]
        temp = float((int(temp, 2))) * 0.125
        global ret
        if (temp > 30)and(ret == 1):
            ret = 0
            sms.message()

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        print(temp)
        self.y.append(temp)  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.
        # up.upload(temp)




if __name__ == '__main__':

    app=QApplication(sys.argv)
    # apply_stylesheet(app, theme='dark_purple.xml')
    mywindow = MyMainWin()


    mywindow.setWindowTitle("电池管理系统")
    mywindow.show()

    app.exec()
