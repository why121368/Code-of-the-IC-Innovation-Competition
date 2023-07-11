import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from mywindow import *
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
    # print(rd.DeviceClose())
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




class MyMainWin(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWin,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Update_battery_status)
        # self.pushButton_7.clicked.connect(self.Save_data)
    def Update_battery_status(self):
        print("houzhiyi")
        self.progressBar_1.setValue(1.2)
        self.progressBar_2.setValue(3)

        x = [0b10000000,
             0b11000000,
             0b10100000,
             0b11100000,
             0b10010000,
             0b11010000,
             0b10110000,
             0b11110000,
             0b10001000,
             0b11001000, ]

        j = 0

        m = [0] * 11
        v = [0] * 11

        for i in x:
            j += 1
            m[j] = dianya(i)

        for i in range(1, 11):
            v[i] = m[i] - m[i - 1]

        self.progressBar_1.setValue(v[1]*100)
        self.progressBar_2.setValue(v[2]*100)
        self.progressBar_3.setValue(v[3]*100)
        self.progressBar_4.setValue(v[4]*100)
        self.progressBar_5.setValue(v[5]*100)
        self.progressBar_6.setValue(v[6]*100)
        self.progressBar_7.setValue(v[7]*100)
        self.progressBar_8.setValue(v[8]*100)
        self.progressBar_9.setValue(v[9]*100)
        self.progressBar_10.setValue(v[10]*100)
        self.progressBar_111.setValue(v[1]*100)

        self.v_1.setText(str( round(v[1],2 ))+'v')
        self.v_2.setText(str(round(v[2], 2)) + 'v')
        self.v_3.setText(str(round(v[3], 2)) + 'v')
        self.v_4.setText(str(round(v[4], 2)) + 'v')
        self.v_5.setText(str(round(v[5], 2)) + 'v')
        self.v_6.setText(str(round(v[6], 2)) + 'v')
        self.v_7.setText(str(round(v[7], 2)) + 'v')
        self.v_8.setText(str(round(v[8], 2)) + 'v')
        self.v_9.setText(str(round(v[9], 2)) + 'v')
        self.v_10.setText(str(round(v[10], 2)) + 'v')
        self.v_111.setText(str(round(v[1], 2)) + 'v')

        data={'电池':[1,2,4,5,6,7,8,9,10],'电压/V':v[1:10]}
        df = pd.DataFrame(data)
        df=df.set_index("电池")
        df.to_excel("data/电池电压.xlsx")
        print('done!')

    # def Save_data(self):



if __name__ == '__main__':

    app=QApplication(sys.argv)
    # apply_stylesheet(app, theme='dark_purple.xml')
    mywindow=MyMainWin()

    mywindow.setWindowTitle("电池管理系统")

    mywindow.show()

    app.exec()
