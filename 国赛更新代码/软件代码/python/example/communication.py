import paramiko
import dataprocessing as proc
# 输入用户名、密码、ip等

# -*- coding: cp936 -*-
import ctypes
import os
import time
#import numpy
from ctypes import *
from ctypes import create_string_buffer
from ctypes import c_buffer
from ctypes import sizeof
# import uptocloud as up

#import pandas
import time

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
    re[0] = w[0]
    re[1] = w[1]
    if re[1] == '':
        re[1] = re[0]
        re[0] = '0'
    return re

#传入字符串地址
def read(address):
    address = address[2:]
    raddr = (c_char * 1)()
    recive = (c_char * 1)()
    Is_True = I2cDriver_dll_Usb.ConfigIICParam(ctypes.c_uint(0), ctypes.c_uint(10000), ctypes.c_uint(0))
    raddr = bytes.fromhex(address)
    recive = b"\x00"
    r = I2cDriver_dll_Usb.IICRegisterRead(ctypes.c_bool(0), ctypes.c_uint(0x08), raddr, recive, ctypes.c_char(1),
                                          ctypes.c_uint(1), ctypes.c_uint(0))
    A = ('%#x' % recive[0])
    print(A)
    result = pre(str(A))
    result = proc.trans(result[0]) + proc.trans(result[1])
    return result

#传入字符串地址和数据
def write(address,data):
    address = address[2:]
    data =data[2:]
    raddr = (c_char * 1)()
    send = (c_char * 1)()
    Is_True = I2cDriver_dll_Usb.ConfigIICParam(ctypes.c_uint(0), ctypes.c_uint(10000), ctypes.c_uint(0))
    raddr = bytes.fromhex(address)
    send = bytes.fromhex(data)
    result = I2cDriver_dll_Usb.IICRegisterSend(ctypes.c_bool(0), ctypes.c_uint(0x08), raddr, send, ctypes.c_char(1),
                                          ctypes.c_uint(1), ctypes.c_uint(0))
    return result


def uart_read():
    A = (c_char * 1)()
    A = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    Uart_true = I2cDriver_dll_Usb.ConfigUARTParam(ctypes.c_uint(115200), ctypes.c_uint(0), ctypes.c_uint(0),
                                                  ctypes.c_uint(0));
    uart_rx = I2cDriver_dll_Usb.UARTRcvData(A, ctypes.c_uint(3), ctypes.c_uint(0))
    A = ('%#x' % A[1])
    result = pre(str(A))
    result = proc.trans(result[0]) + proc.trans(result[1])
    return result


def uart_send(data):
    data =data[2:]
    A = (c_char * 1)()
    A = bytes.fromhex(data)
    Uart_true = I2cDriver_dll_Usb.ConfigUARTParam(ctypes.c_uint(115200), ctypes.c_uint(0), ctypes.c_uint(0),
                                                  ctypes.c_uint(0));
    uart_tx = I2cDriver_dll_Usb.UARTSendData(A, ctypes.c_uint(1), ctypes.c_uint(0))



def temp():
    raddr1 = (c_char * 1)()
    raddr2 = (c_char * 1)()
    send = (c_char * 1)()
    recive = (c_char * 2)()

    raddr2 = b"\x00"
    recive = b"\x00\x00"
    r = I2cDriver_dll_Usb.IICRegisterRead(ctypes.c_bool(0), ctypes.c_uint(0x48), raddr2, recive, ctypes.c_char(1),
                                          ctypes.c_uint(2), ctypes.c_uint(0))
    A = ('%#x' % recive[0])
    B = ('%#x' % recive[1])
    result = pre(str(A))
    result1 = proc.trans(result[0]) + proc.trans(result[1])
    result = pre(str(B))
    result2 = proc.trans(result[0]) + proc.trans(result[1])
    temp = result1 + result2[0:3]
    temp = float((int(temp, 2))) * 0.125
    return temp

# uart_send('0x00')
# time.sleep(1)
# a = uart_read()
# print(a)
# if(a == '11000001'):
#     uart_send('0x85')


#
#
# i = 1
# while (i == 1):
#     uart_send('0x00')
#     # time.sleep(0.5)
#     a = uart_read()
#     print(a)
#     if (a == '11000001'):#开启警报灯
#         uart_send('0x85')
#     if (a == '10000010'):#关闭警报灯
#         uart_send('0x84')
#     if (a == '11000000'):#警报解除
#         uart_send('0x88')
#     if (a == '00100000'):#开启警报
#         uart_send('0x89')
#     # time.sleep(1)

