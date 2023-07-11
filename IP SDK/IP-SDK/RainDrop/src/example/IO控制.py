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

def dianya():

    py_path, py_name = os.path.split(os.path.abspath(__file__))

    base_dir = pathlib.Path(py_path).absolute().parent  # sys.argv[0]

    if sys.path.count(base_dir) == 0:
        sys.path.append(str(base_dir))
    # rd = RD()
    # rd.DeviceEnumLists()
    # print(rd.devicelist)
    # rd.DeviceOpen(0)

    # analogIn config

    in_ch = 0  # 0 or 1 for channel 1 or 2
    in_ch2 = 1
    in_range = 5  # 5 or 25
    in_range2 = 25  # not use until use double chs
    in_fre = 1e6
    trig_timeout = 0  # 0 for forever, 1 for 1s
    trig_src = RDTRIGSRCNone  # RDTRIGSRCDetectorAnalogInCH1 for anlogout channel 1
    trig_type = RDTRIGTYPEEdge
    trig_leve = 0
    trig_slope = RDTriggerSlopeEdge
    buffersize = 2048

    rd.AnalogInCHEnable(in_ch, True)
    rd.AnalogInCHRangeSet(in_ch, in_range2)
    rd.AnalogInCHEnable(in_ch2, True)
    rd.AnalogInCHRangeSet(in_ch2, in_range)
    rd.AnalogInFrequencySet(in_fre)
    rd.AnalogInTriggerAutoTimeoutSet(trig_timeout)
    rd.AnalogInTriggerSourceSet(trig_src)
    rd.AnalogInTriggerTypeSet(trig_type)
    rd.AnalogInTriggerLevelSet(trig_leve, in_range)  # (trig_src==RDTRIGSRCDetectorAnalogInCH1)?in_range:in_range2
    rd.AnalogInTriggerConditionSet(trig_slope)
    rd.AnalogInBufferSizeSet(buffersize)
    rd.AnalogInRun(True)

    # analogIn status read
    rd.AnalogInStatus()
    i = 0
    while (rd.analoginstatus != 2) & (i < 10):
        rd.AnalogInStatus()
        i = i + 1
        # print(rd.analoginstatus)

    # analogIn data read
    if (rd.analoginstatus == 2):
        rd.AnalogInRead(buffersize, 0)
        rd.AnalogInRead(buffersize, 1)
        # print(rd.aibacksizech1, rd.aibacksizech2)
        value = list(rd.aidatach1)  # the ch1 scope data as c_char_p(4086)  don't use rd.aidatach1.value
        plt.plot(value)
        # value = list(rd.aidatach2)  # the ch1 scope data as c_char_p(4086)  don't use rd.aidatach1.value
        # plt.plot(value)
        # print(value)
        sum = 0
        x = 0
        for i in value:
            x += 1
            sum += i

        value1 = sum / x
        # print(value1)

        # plt.show()

    # close all instruments
    rd.AnalogInRun(False)
    # close connect
    rd.DeviceClose()
    return value1


x=[0b10000000,
   0b11000000,
   0b10100000,
   0b11100000,
   0b10010000,
   0b11010000,
   0b10110000,
   0b11110000,
   0b10001000,
   0b11001000,]

j=0

m=[0]*11
v=[0]*11

for i in x:
    j +=1
    rd = RD()
    rd.DeviceEnumLists()
    print(rd.devicelist)
    print(rd.DeviceOpen(0))
    # Supplies
    CHs_OUT = 0b11111111  # DIO0 enable output
    CHs_OUTValue = i  # DIO0 output value set high




    rd.DigitalIOOutputEnableSet(CHs_OUT)
    rd.DigitalIOOutputSet(CHs_OUTValue)
    rd.DigitalIOInputStatus()  # first reading drop
    # print(rd.DeviceClose())
    m[j]=dianya()

print(m)
for i in range(1,10):
    v[i]=m[i]-m[i-1]
print(v)


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
# close connect
# print(rd.DeviceClose())