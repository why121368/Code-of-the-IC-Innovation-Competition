# -*- coding: cp936 -*-
import ctypes
import os
import time
#import numpy
from ctypes import *
from ctypes import create_string_buffer
from ctypes import c_buffer
from ctypes import sizeof

#import pandas

#AbsPath  = os.path.abspath(os.path.dirname(__file__))
Dir_USB2UARTSPIIICDLL = "USB2UARTSPIIICDLL.dll"
print(Dir_USB2UARTSPIIICDLL)

#导入动态链接库
#64位
I2cDriver_dll_Usb = ctypes.CDLL(Dir_USB2UARTSPIIICDLL,winmode=0)
#32位
#SpiDriver_dll_Usb = ctypes.windll.LoadLibrary(Dir_USB2UARTSPIIICDLL)
#打开端口
Is_Open  = I2cDriver_dll_Usb.OpenUsb(ctypes.c_int(0))
print(Is_Open)

Uart_true = I2cDriver_dll_Usb.ConfigUARTParam(ctypes.c_uint(115200),ctypes.c_uint(0),ctypes.c_uint(0),ctypes.c_uint(0));
print('Uart 配置')
print(Uart_true)

A = (c_char * 1)()
A = b"\x06"

uart_tx =I2cDriver_dll_Usb.UARTSendData(A,ctypes.c_uint(1),ctypes.c_uint(0))
print('是否发送：'+str(uart_tx))




