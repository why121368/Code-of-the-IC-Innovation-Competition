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

#配置参数

Is_True = I2cDriver_dll_Usb.ConfigIICParam(ctypes.c_uint(0),ctypes.c_uint(10000),ctypes.c_uint(0))
print(Is_True)

print('初始化完成')

#发送数据
raddr1 = (c_char * 1)()
raddr2 = (c_char * 1)()
send = (c_char * 1)()
recive = (c_char * 1)()


raddr1 = b"\x06"
raddr2 = b"\x00"
send= b"\x9f"
recive = b"\x00"

#
# #IICRegisterSend(unsigned char addrMod,unsigned int addr,unsigned char *regBuf,unsigned char *sendBuf,unsigned char reglen,unsigned int slen,unsigned int UsbIndex);
# #IICRegisterRead(unsigned char addrMod,unsigned int addr,unsigned char *regBuf,unsigned char *rcvBuf,unsigned char reglen,unsigned int rlen,unsigned int UsbIndex);
s = I2cDriver_dll_Usb.IICRegisterSend(ctypes.c_bool(0),ctypes.c_uint(0x48),raddr1,send,ctypes.c_char(1),ctypes.c_uint(1),ctypes.c_uint(0))
r = I2cDriver_dll_Usb.IICRegisterRead(ctypes.c_bool(0),ctypes.c_uint(0x48),raddr2,recive,ctypes.c_char(1),ctypes.c_uint(2),ctypes.c_uint(0))

print('%#x'%recive[0])

Uart_true = I2cDriver_dll_Usb.ConfigUARTParam(ctypes.c_uint(115200),ctypes.c_uint(0),ctypes.c_uint(0),ctypes.c_uint(0));
print('Uart 配置')
print(Uart_true)

A = (c_char * 1)()
A = b"\x06"

uart_tx =I2cDriver_dll_Usb.UARTSendData(A,ctypes.c_uint(1),ctypes.c_uint(0))
print('是否发送：'+str(uart_tx))




