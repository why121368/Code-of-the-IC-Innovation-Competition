# -*- coding: cp936 -*-
import ctypes
import os
import time
#import numpy
from ctypes import *
from ctypes import create_string_buffer
from ctypes import c_buffer
from ctypes import sizeof
import uptocloud as up

#import pandas
import time

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

#���ò���

Is_True = I2cDriver_dll_Usb.ConfigIICParam(ctypes.c_uint(0),ctypes.c_uint(10000),ctypes.c_uint(0))
print(Is_True)

print('��ʼ�����')

#��������
raddr1 = (c_char * 1)()
raddr2 = (c_char * 1)()
send = (c_char * 1)()
recive = (c_char * 2)()


# raddr2 = b"\x00"
# recive= b"\x00\x00"


raddr2 = bytes([0x00])
recive= bytes([0x00,0x00])

print(type(recive))


#
# #IICRegisterSend(unsigned char addrMod,unsigned int addr,unsigned char *regBuf,unsigned char *sendBuf,unsigned char reglen,unsigned int slen,unsigned int UsbIndex);
# #IICRegisterRead(unsigned char addrMod,unsigned int addr,unsigned char *regBuf,unsigned char *rcvBuf,unsigned char reglen,unsigned int rlen,unsigned int UsbIndex);
# s = I2cDriver_dll_Usb.IICRegisterSend(ctypes.c_bool(0),ctypes.c_uint(0x48),raddr1,send,ctypes.c_char(1),ctypes.c_uint(1),ctypes.c_uint(0))

for i in range(0,100):

    r = I2cDriver_dll_Usb.IICRegisterRead(ctypes.c_bool(0),ctypes.c_uint(0x48),raddr2,recive,ctypes.c_char(1),ctypes.c_uint(2),ctypes.c_uint(0))
    print('%#x'%recive[0])
    print('%#x'%recive[1])
    time.sleep(1)






