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

#���붯̬���ӿ�
#64λ
I2cDriver_dll_Usb = ctypes.CDLL(Dir_USB2UARTSPIIICDLL,winmode=0)
#32λ
#SpiDriver_dll_Usb = ctypes.windll.LoadLibrary(Dir_USB2UARTSPIIICDLL)
#�򿪶˿�
Is_Open  = I2cDriver_dll_Usb.OpenUsb(ctypes.c_int(0))
print(Is_Open)

Uart_true = I2cDriver_dll_Usb.ConfigUARTParam(ctypes.c_uint(115200),ctypes.c_uint(0),ctypes.c_uint(0),ctypes.c_uint(0));
print('Uart ����')
print(Uart_true)

A = (c_char * 1)()
A = b"\x06"

uart_tx =I2cDriver_dll_Usb.UARTSendData(A,ctypes.c_uint(1),ctypes.c_uint(0))
print('�Ƿ��ͣ�'+str(uart_tx))




