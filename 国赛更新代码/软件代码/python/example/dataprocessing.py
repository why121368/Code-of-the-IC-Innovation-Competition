import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib.pyplot as plt
import numpy as np
import time
import sys, os
import pathlib
# from PySide6 import QtWidgets
# from PySide2 import QtWidgets
from PyQt5 import QtWidgets
from qt_material import apply_stylesheet
import matplotlib.pyplot as plt
import pandas as pd
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
def max(a,b):
    if a > b:
        return 1
    else:
        return 0

def min(a,b):
    if a < b:
        return 1
    else:
        return 0

def color(m):
    if m == '0':
        str = "background-color: rgb(170, 255, 0);"
    if m == '1':
        str = "background-color: rgb(85, 170, 255);"
    if m == '2':
        str = "background-color: rgb(255, 0, 0);"
    if m == '3':
        str = "background-color: rgb(0, 255, 127);"
    return str
def trans(a):
    b= bin(int(a,16))[2:]
    lenth = len(b)
    b = (4-lenth)*'0'+b
    return b

def Error(a,b):
    a = abs(a)
    if a <= b:
        str = '3'
    if a > b:
        str = '2'
    return str


def save_state(v,m,n):
    data = {'电池': [1, 2, 4, 5, 6, 7, 8, 9, 10], '电压/V': v[1:10]}
    df = pd.DataFrame(data)
    df.to_excel("data/电池电压.xlsx")
    print('done')



def voltage():
    s=pd.read_excel("./data/电池数据.xlsx")

    v = list(s['真实值/V'])
    print(v)
    v1 = list(s['测试值/V'])
    v3 = list(s['误差值/V'])
    species = ("ch1", "ch2", "ch3","ch4","ch5","ch6","ch7","ch8","ch9","ch10")
    penguin_means = {
        'True value': v,
        'Test value': v1,
        'Error value': v3,
    }

    x = np.arange(len(species))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0
    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Voltage (V)')
    ax.set_title('Voltage detection function test results')
    ax.set_xticks(x + width, species)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 2)

    fig.set_figheight(4)
    fig.set_figwidth(10)
    plt.savefig('./data/voltage.png')

def Current(z,c):
    a = z
    a1 = c
    a3 = z-c
    species = ("True value", "Test value", "Error value")
    penguin_means = {
        'True value': (a,a1,a3)
    }

    x = np.arange(len(species))  # the label locations
    width = 0.5  # the width of the bars
    multiplier = 0
    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Voltage (V)')
    ax.set_title('Voltage detection function test results')
    ax.set_xticks(x + width, species)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 6)

    fig.set_figheight(4)
    fig.set_figwidth(6)
    plt.savefig('./data/current.png')


def wendu(z,c):
    a = z
    a1 = c
    a3 = z-c
    species = ("True value", "Test value", "Error value")
    penguin_means = {
        'True value': (a,a1,a3)
    }

    x = np.arange(len(species))  # the label locations
    width = 0.5  # the width of the bars
    multiplier = 0
    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Voltage (V)')
    ax.set_title('Voltage detection function test results')
    ax.set_xticks(x + width, species)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 60)

    fig.set_figheight(4)
    fig.set_figwidth(6)
    plt.savefig('./data/wendu.png')


def dianya(i):
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
    py_path, py_name = os.path.split(os.path.abspath(__file__))

    base_dir = pathlib.Path(py_path).absolute().parent  # sys.argv[0]

    if sys.path.count(base_dir) == 0:
        sys.path.append(str(base_dir))


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
    i = 0
    rd.DigitalIOOutputEnableSet(CHs_OUT)
    rd.DigitalIOOutputSet(CHs_OUTValue)
    rd.DigitalIOInputStatus()  # first reading drop
    time.sleep(3)
    while (rd.analoginstatus != 2) & (i < 10):
        rd.AnalogInStatus()
        i = i + 1


    # analogIn data read
    if (rd.analoginstatus == 2):
        rd.AnalogInRead(buffersize, 0)
        rd.AnalogInRead(buffersize, 1)
        # print(rd.aibacksizech1, rd.aibacksizech2)
        # value = list(rd.aidatach1)  # the ch1 scope data as c_char_p(4086)  don't use rd.aidatach1.value
        # plt.plot(value)
        value = list(rd.aidatach2)  # the ch1 scope data as c_char_p(4086)  don't use rd.aidatach1.value


    # close all instruments
    rd.AnalogInRun(False)
    # close connect
    rd.DeviceClose()
    return value

def CHG():
    value1 = dianya(0b00000010)
    value2 = dianya(0b00000000)
    value3 = value1 + value2
    fig = plt.plot(value3)
    plt.ylim(-3,6)
    plt.savefig('./data/wave.png')

