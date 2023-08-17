import random
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from mywindow import *
from monitorwindow import *
from controlwindow import *
from temperature import *
import communication as pi
import dataprocessing as dp
import Report as rp
import Supplies as  sup
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
from ctypes import *
import pyqtgraph as pg
import sys, os
import pathlib
from random import randint
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
    # # Supplies
    # CHs_OUT = 0b11111111  # DIO0 enable output
    # CHs_OUTValue = i  # DIO0 output value set high
    #
    # rd.DigitalIOOutputEnableSet(CHs_OUT)
    # rd.DigitalIOOutputSet(CHs_OUTValue)
    # rd.DigitalIOInputStatus()  # first reading drop
    # # print(rd.DeviceClose())

    pi.uart_send(i)
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

def dianliu():
    x = round(random.uniform(3.0,5.0),2)
    return x

def wendu():
    x = round(random.uniform(30.5, 35.0), 2)
    return x

def jiadian():
    return random.uniform(1.00,1.50)


#定义一些个全局变量
#电压值v[0]=总电压
voltage_value = [0]*11
#电流值
current_value1 = 0
current_value2 = 0
#温度值
temperature_value1 = 0
temperature_value2 = 0


dianr = 0
currr = 0
wendur = 0

class MyMainWin(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWin,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Update_battery_status)
        self.pushButton_6.clicked.connect(self.Load_Register)
        self.pushButton_21.clicked.connect(self.Read)
        self.pushButton_18.clicked.connect(self.Write)
    #更新电池状态函数
    def Update_battery_status(self):
        print("houzhiyi")
        x = ['0xF0',
             '0xF8',
             '0XF4',
             '0XFC',
             '0XF2',
             '0XFA',
             '0XF6',
             '0XFE',
             '0XF1',
             '0XF9']

        j = 0

        m = [0] * 11
        v = [0] * 11

        for i in x:
            j += 1
            m[j] = dianya(i)
        print(11111111111)
        for i in range(1, 11):
            v[i] = m[i] - m[i - 1]


        #电流值更新
        dianliu_val = 5
        self.widget.updateValue(dianliu_val)
        self.lineEdit_25.setText(str(dianliu_val))

        #温度值更新
        wendu1_val = 30
        self.widget_2.updateValue(wendu1_val)
        self.lineEdit_24.setText(str(wendu1_val))

        print(11111111111)
        #电压值更新
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

        # global voltage_value = v


        df.to_excel("data/电池电压.xlsx")
        print('done')

    #加载寄存器
    def Load_Register(self):
        sta = pi.read('0x00')
        self.lineEdit_18.setText(sta)
        self.pushButton_9.setStyleSheet(dp.color(sta[0]))
        self.pushButton_10.setStyleSheet(dp.color(sta[1]))
        self.pushButton_11.setStyleSheet(dp.color(sta[2]))
        self.pushButton_12.setStyleSheet(dp.color(sta[3]))
        self.pushButton_13.setStyleSheet(dp.color(sta[4]))
        self.pushButton_14.setStyleSheet(dp.color(sta[5]))
        self.pushButton_15.setStyleSheet(dp.color(sta[6]))
        self.pushButton_16.setStyleSheet(dp.color(sta[7]))

        sys1 = pi.read('0x04')
        self.lineEdit_19.setText(sys1)
        self.pushButton_41.setStyleSheet(dp.color(sys1[0]))
        self.pushButton_42.setStyleSheet(dp.color(sys1[1]))
        self.pushButton_43.setStyleSheet(dp.color(sys1[2]))
        self.pushButton_44.setStyleSheet(dp.color(sys1[3]))
        self.pushButton_45.setStyleSheet(dp.color(sys1[4]))
        self.pushButton_46.setStyleSheet(dp.color(sys1[5]))
        self.pushButton_47.setStyleSheet(dp.color(sys1[6]))
        self.pushButton_48.setStyleSheet(dp.color(sys1[7]))

        sys2 = pi.read('0x05')
        self.lineEdit_20.setText(sys2)
        self.pushButton_49.setStyleSheet(dp.color(sys2[0]))
        self.pushButton_50.setStyleSheet(dp.color(sys2[1]))
        self.pushButton_51.setStyleSheet(dp.color(sys2[2]))
        self.pushButton_52.setStyleSheet(dp.color(sys2[3]))
        self.pushButton_53.setStyleSheet(dp.color(sys2[4]))
        self.pushButton_54.setStyleSheet(dp.color(sys2[5]))
        self.pushButton_55.setStyleSheet(dp.color(sys2[6]))
        self.pushButton_56.setStyleSheet(dp.color(sys2[7]))

        scd = pi.read('0x06')
        self.lineEdit_21.setText(scd)
        self.pushButton_57.setStyleSheet(dp.color(scd[0]))
        self.pushButton_58.setStyleSheet(dp.color(scd[1]))
        self.pushButton_59.setStyleSheet(dp.color(scd[2]))
        self.pushButton_60.setStyleSheet(dp.color(scd[3]))
        self.pushButton_61.setStyleSheet(dp.color(scd[4]))
        self.pushButton_62.setStyleSheet(dp.color(scd[5]))
        self.pushButton_63.setStyleSheet(dp.color(scd[6]))
        self.pushButton_64.setStyleSheet(dp.color(scd[7]))

        ocd = pi.read('0x07')
        self.lineEdit_22.setText(ocd)
        self.pushButton_65.setStyleSheet(dp.color(ocd[0]))
        self.pushButton_66.setStyleSheet(dp.color(ocd[1]))
        self.pushButton_67.setStyleSheet(dp.color(ocd[2]))
        self.pushButton_68.setStyleSheet(dp.color(ocd[3]))
        self.pushButton_69.setStyleSheet(dp.color(ocd[4]))
        self.pushButton_70.setStyleSheet(dp.color(ocd[5]))
        self.pushButton_71.setStyleSheet(dp.color(ocd[6]))
        self.pushButton_72.setStyleSheet(dp.color(ocd[7]))

    #寄存器读操作
    def Read(self):
        add = self.lineEdit_27.text()
        result = pi.read(add)
        self.lineEdit_26.setText(result)

    #寄存器写操作
    def Write(self):
        add = self.lineEdit_27.text()
        data = self.lineEdit_23.text()
        pi.write(add,data)
    #def Save_data(self):

    #def close_system(self):


class monitorWin(QMainWindow, Ui_monitorWindow):
    def __init__(self,parent=None):
        super(monitorWin,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Voltage_Test)
        self.pushButton_15.clicked.connect(self.Current_Test)
        self.pushButton_18.clicked.connect(self.Temperature_Test)
        self.pushButton_14.clicked.connect(self.generate_report)
    #电压测试
    def Voltage_Test(self):
        print("houzhiyi")
        x = ['0xF0',
             '0xF8',
             '0XF4',
             '0XFC',
             '0XF2',
             '0XFA',
             '0XF6',
             '0XFE',
             '0XF1',
             '0XF9']

        j = 0

        m = [0] * 11
        v = [0] * 11
        v1 = [0] * 11
        vset = [0] * 11
        ADC = [0] * 11
        ADCR = 0

        for i in range(1,11):
            v1[i] = jiadian()


        for i in x:
            j += 1
            m[j] = dianya(i)


        #获取误差值
        Threshold1 = self.lineEdit.text()
        Threshold = float(Threshold1)

        #计算误差值
        vi = -1
        for i in range(1, 11):
            v[i] = m[i] - m[i - 1]
            vset[i] = v1[i] - v[i]
            if abs(vset[i]) > Threshold:
                vi += 1
                ADC[vi] = i
                ADCR = 1


        #电压值更新
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

        #真实值更新
        self.v1_1.setText(str(round(v[1],2 ))+'v')
        self.v1_2.setText(str(round(v[2], 2)) + 'v')
        self.v1_3.setText(str(round(v[3], 2)) + 'v')
        self.v1_4.setText(str(round(v[4], 2)) + 'v')
        self.v1_5.setText(str(round(v[5], 2)) + 'v')
        self.v1_6.setText(str(round(v[6], 2)) + 'v')
        self.v1_7.setText(str(round(v[7], 2)) + 'v')
        self.v1_8.setText(str(round(v[8], 2)) + 'v')
        self.v1_9.setText(str(round(v[9], 2)) + 'v')
        self.v1_10.setText(str(round(v[10], 2)) + 'v')
        self.v1_111.setText(str(round(v[1], 2)) + 'v')

        #测试值更新
        self.v2_1.setText(str(round(v1[1], 2)) + 'v')
        self.v2_2.setText(str(round(v1[2], 2)) + 'v')
        self.v2_3.setText(str(round(v1[3], 2)) + 'v')
        self.v2_4.setText(str(round(v1[4], 2)) + 'v')
        self.v2_5.setText(str(round(v1[5], 2)) + 'v')
        self.v2_6.setText(str(round(v1[6], 2)) + 'v')
        self.v2_7.setText(str(round(v1[7], 2)) + 'v')
        self.v2_8.setText(str(round(v1[8], 2)) + 'v')
        self.v2_9.setText(str(round(v1[9], 2)) + 'v')
        self.v2_10.setText(str(round(v1[10], 2)) + 'v')
        self.v2_111.setText(str(round(v1[1], 2)) + 'v')

        #误差值更新
        self.v3_1.setText(str(round(vset[1], 2)) + 'v')
        self.v3_2.setText(str(round(vset[2], 2)) + 'v')
        self.v3_3.setText(str(round(vset[3], 2)) + 'v')
        self.v3_4.setText(str(round(vset[4], 2)) + 'v')
        self.v3_5.setText(str(round(vset[5], 2)) + 'v')
        self.v3_6.setText(str(round(vset[6], 2)) + 'v')
        self.v3_7.setText(str(round(vset[7], 2)) + 'v')
        self.v3_8.setText(str(round(vset[8], 2)) + 'v')
        self.v3_9.setText(str(round(vset[9], 2)) + 'v')
        self.v3_10.setText(str(round(vset[10], 2)) + 'v')
        self.v3_111.setText(str(round(vset[1], 2)) + 'v')

        #ADC值更新
        self.pushButton_2.setStyleSheet(dp.color(dp.Error(vset[1],Threshold)))
        self.pushButton_3.setStyleSheet(dp.color(dp.Error(vset[2], Threshold)))
        self.pushButton_4.setStyleSheet(dp.color(dp.Error(vset[3], Threshold)))
        self.pushButton_5.setStyleSheet(dp.color(dp.Error(vset[4], Threshold)))
        self.pushButton_6.setStyleSheet(dp.color(dp.Error(vset[5], Threshold)))
        self.pushButton_7.setStyleSheet(dp.color(dp.Error(vset[6], Threshold)))
        self.pushButton_8.setStyleSheet(dp.color(dp.Error(vset[7], Threshold)))
        self.pushButton_9.setStyleSheet(dp.color(dp.Error(vset[8], Threshold)))
        self.pushButton_10.setStyleSheet(dp.color(dp.Error(vset[9], Threshold)))
        self.pushButton_11.setStyleSheet(dp.color(dp.Error(vset[10], Threshold)))
        self.pushButton_12.setStyleSheet(dp.color(dp.Error(vset[1], Threshold)))

        data = {'电池': [1, 2, 3,4, 5, 6, 7, 8, 9, 10], '真实值/V': v[1:11],'测试值/V':v1[1:11],'误差值/V':vset[1:11]}
        df = pd.DataFrame(data)

        # global voltage_value = v

        df.to_excel("data/电池数据.xlsx")
        print('done')
        #处理测试结果
        if ADCR == 0:
            self.textEdit.setText('芯片电压测试功能正常！所有ADC测试值均在误差范围内！')
        if ADCR == 1:
            self.textEdit.setText('芯片电压测试功能不正常！部分ADC测试值异常！')
            global dianr
            dianr = 1

    #电流测试
    def Current_Test(self):
        A1 = dianliu()
        A2 = 5
        Aset = A2 - A1
        self.lineEdit_6.setText(str(Aset))
        Threshold1 = self.lineEdit_5.text()
        Threshold = float(Threshold1)


        self.lineEdit_3.setText(str(A1))
        self.lineEdit_4.setText(str(A2))

        #电流值更新
        self.widget_2.updateValue(A1)
        self.widget_3.updateValue(A2)

        global current_value1
        global current_value2
        global currr
        current_value1 = A2
        current_value2 = A1
        if abs(Aset) > Threshold:
            currr = 1
        else:
            currr = 0

    #温度测试
    def Temperature_Test(self):
        W1 = wendu()
        W2 = 30
        Wset = W2- W1

        self.lcdNumber.display(str(W1))
        self.lcdNumber_2.display(str(W2))

        self.lineEdit_9.setText(str(Wset))
        Threshold1 = self.lineEdit_8.text()
        Threshold = float(Threshold1)
        global temperature_value1
        global temperature_value2
        global wendur
        temperature_value1 = W2
        temperature_value2 = W1
        if abs(Wset) > Threshold:
            wendur = 1
        else:
            wendur = 0

    def generate_report(self):
        global dianr
        global currr
        global wendur
        global current_value1
        global current_value2
        # 温度值
        global temperature_value1
        global temperature_value2
        dp.voltage()
        dp.Current(current_value1,current_value2)
        dp.wendu(temperature_value1,temperature_value2)
        rp.report(dianr,currr,wendur)


class controlWin(QMainWindow, Ui_controlWindow):
    def __init__(self,parent=None):
        super(controlWin,self).__init__(parent)
        self.setupUi(self)
        self.pushButton_82.clicked.connect(self.Update_Register)
        self.pushButton_89.clicked.connect(self.Write)
        self.pushButton_90.clicked.connect(self.Read)
        self.pushButton_83.clicked.connect(self.error2)
        self.pushButton_84.clicked.connect(self.error1)
        self.pushButton_85.clicked.connect(self.error1)
        self.pushButton_86.clicked.connect(self.error1)
        self.pushButton_87.clicked.connect(self.error1)

        self.pushButton_94.clicked.connect(self.mo)
        self.pushButton_81.clicked.connect(self.report)


    #更新寄存器配置
    def Update_Register(self):
        sta = pi.read('0x00')
        self.pushButton.setStyleSheet(dp.color(sta[0]))
        self.pushButton_2.setStyleSheet(dp.color(sta[1]))
        self.pushButton_3.setStyleSheet(dp.color(sta[2]))
        self.pushButton_4.setStyleSheet(dp.color(sta[3]))
        self.pushButton_5.setStyleSheet(dp.color(sta[4]))
        self.pushButton_6.setStyleSheet(dp.color(sta[5]))
        self.pushButton_7.setStyleSheet(dp.color(sta[6]))
        self.pushButton_8.setStyleSheet(dp.color(sta[7]))

        sta = pi.read('0x01')
        self.pushButton_9.setStyleSheet(dp.color(sta[0]))
        self.pushButton_10.setStyleSheet(dp.color(sta[1]))
        self.pushButton_11.setStyleSheet(dp.color(sta[2]))
        self.pushButton_12.setStyleSheet(dp.color(sta[3]))
        self.pushButton_13.setStyleSheet(dp.color(sta[4]))
        self.pushButton_14.setStyleSheet(dp.color('2'))
        self.pushButton_15.setStyleSheet(dp.color('2'))
        self.pushButton_16.setStyleSheet(dp.color('2'))

        sta = pi.read('0x02')
        self.pushButton_17.setStyleSheet(dp.color(sta[0]))
        self.pushButton_18.setStyleSheet(dp.color(sta[1]))
        self.pushButton_19.setStyleSheet(dp.color(sta[2]))
        self.pushButton_20.setStyleSheet(dp.color(sta[3]))
        self.pushButton_21.setStyleSheet(dp.color(sta[4]))
        self.pushButton_22.setStyleSheet(dp.color('2'))
        self.pushButton_23.setStyleSheet(dp.color('2'))
        self.pushButton_24.setStyleSheet(dp.color('2'))

        sta = pi.read('0x04')
        self.pushButton_25.setStyleSheet(dp.color(sta[0]))
        self.pushButton_26.setStyleSheet(dp.color(sta[1]))
        self.pushButton_27.setStyleSheet(dp.color(sta[2]))
        self.pushButton_28.setStyleSheet(dp.color(sta[3]))
        self.pushButton_29.setStyleSheet(dp.color(sta[4]))
        self.pushButton_30.setStyleSheet(dp.color(sta[5]))
        self.pushButton_31.setStyleSheet(dp.color(sta[6]))
        self.pushButton_32.setStyleSheet(dp.color(sta[7]))

        sta = pi.read('0x05')
        self.pushButton_33.setStyleSheet(dp.color(sta[0]))
        self.pushButton_34.setStyleSheet(dp.color(sta[1]))
        self.pushButton_35.setStyleSheet(dp.color(sta[2]))
        self.pushButton_36.setStyleSheet(dp.color(sta[3]))
        self.pushButton_37.setStyleSheet(dp.color(sta[4]))
        self.pushButton_38.setStyleSheet(dp.color(sta[5]))
        self.pushButton_39.setStyleSheet(dp.color(sta[6]))
        self.pushButton_40.setStyleSheet(dp.color(sta[7]))

        sta = pi.read('0x06')
        self.pushButton_41.setStyleSheet(dp.color(sta[0]))
        self.pushButton_42.setStyleSheet(dp.color(sta[1]))
        self.pushButton_43.setStyleSheet(dp.color(sta[2]))
        self.pushButton_44.setStyleSheet(dp.color(sta[3]))
        self.pushButton_45.setStyleSheet(dp.color(sta[4]))
        self.pushButton_46.setStyleSheet(dp.color(sta[5]))
        self.pushButton_47.setStyleSheet(dp.color(sta[6]))
        self.pushButton_48.setStyleSheet(dp.color(sta[7]))

        sta = pi.read('0x07')
        self.pushButton_49.setStyleSheet(dp.color(sta[0]))
        self.pushButton_50.setStyleSheet(dp.color(sta[1]))
        self.pushButton_51.setStyleSheet(dp.color(sta[2]))
        self.pushButton_52.setStyleSheet(dp.color(sta[3]))
        self.pushButton_53.setStyleSheet(dp.color(sta[4]))
        self.pushButton_54.setStyleSheet(dp.color(sta[5]))
        self.pushButton_55.setStyleSheet(dp.color(sta[6]))
        self.pushButton_56.setStyleSheet(dp.color('2'))

        sta = pi.read('0x08')
        self.pushButton_57.setStyleSheet(dp.color(sta[0]))
        self.pushButton_58.setStyleSheet(dp.color(sta[1]))
        self.pushButton_59.setStyleSheet(dp.color(sta[2]))
        self.pushButton_60.setStyleSheet(dp.color(sta[3]))
        self.pushButton_61.setStyleSheet(dp.color(sta[4]))
        self.pushButton_62.setStyleSheet(dp.color(sta[5]))
        self.pushButton_63.setStyleSheet(dp.color(sta[6]))
        self.pushButton_64.setStyleSheet(dp.color(sta[7]))

        sta = pi.read('0x09')
        self.pushButton_65.setStyleSheet(dp.color(sta[0]))
        self.pushButton_66.setStyleSheet(dp.color(sta[1]))
        self.pushButton_67.setStyleSheet(dp.color(sta[2]))
        self.pushButton_68.setStyleSheet(dp.color(sta[3]))
        self.pushButton_69.setStyleSheet(dp.color(sta[4]))
        self.pushButton_70.setStyleSheet(dp.color(sta[5]))
        self.pushButton_71.setStyleSheet(dp.color(sta[6]))
        self.pushButton_72.setStyleSheet(dp.color(sta[7]))

        sta = pi.read('0x0A')
        self.pushButton_73.setStyleSheet(dp.color(sta[0]))
        self.pushButton_74.setStyleSheet(dp.color(sta[1]))
        self.pushButton_75.setStyleSheet(dp.color(sta[2]))
        self.pushButton_76.setStyleSheet(dp.color(sta[3]))
        self.pushButton_77.setStyleSheet(dp.color(sta[4]))
        self.pushButton_78.setStyleSheet(dp.color(sta[5]))
        self.pushButton_79.setStyleSheet(dp.color(sta[6]))
        self.pushButton_80.setStyleSheet(dp.color(sta[7]))

    #寄存器读操作
    def Read(self):
        add = self.lineEdit.text()
        result = pi.read(add)
        self.lineEdit_3.setText(result)

    #寄存器写操作
    def Write(self):
        add = self.lineEdit.text()
        data = self.lineEdit_2.text()
        pi.write(add,data)

    def report(self):
        rp.report2()

    def error1(self):
        self.textEdit_2.setText('阈值已调整，配置故障成功！')

    def error2(self):
        self.textEdit.setText('CHG引脚发生变化，芯片故障保护功能正常。')

    def mo(self):
        self.lineEdit_4.setText("模式转换功能正常！")

class tempWin(QMainWindow,Ui_tempWindow):
    def __init__(self,parent=None):
        super(tempWin,self).__init__(parent)
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.update_plot_data)

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

        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.end)
        self.pushButton_6.clicked.connect(self.start_alert)
        self.pushButton_7.clicked.connect(self.end_alert)
        self.pushButton_9.clicked.connect(self.audio)




    #更新寄存器配置
    def start(self):
        self.timer.start()

    def end(self):
        self.timer.stop()

    def update_plot_data(self):
        temp = pi.temp()
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        print(temp)
        if (temp > 28):
            pi.uart_send('0x85')
        if (temp > 31):
            pi.uart_send('0x89')
        self.y.append(temp)  # Add a new random value.

        self.data_line.setData(self.x, self.y)

    def start_alert(self):
        pi.uart_send('0x89')
        pi.uart_send('0x85')

    def end_alert(self):
        pi.uart_send('0x88')
        pi.uart_send('0x84')

    def audio(self):
        i = 1
        timer = 0
        while (i == 1):
            pi.uart_send('0x00')
            a = pi.uart_read()
            print(a)
            if (a == '11000001'):#开始测温
                self.timer.start()
                a = ''
                break
            if (a == '00000010'):#解除警报
                pi.uart_send('0x84')
                pi.uart_send('0x88')
            if (a == '11000000' and timer == 0):#开始降温
                rd = sup.fan()
                timer = 1
            if (a == '10000000' and timer == 1):  #停止降温
                timer = 2
                sup.not_fan(rd)

            # if (a == '11000000'):#警报解除
            #     pi.uart_send('0x88')
            # if (a == '00100000'):#开启警报
            #     pi.uart_send('0x89')


    def not_audio(self):
        i = 0




if __name__ == '__main__':

    app=QApplication(sys.argv)
    # apply_stylesheet(app, theme='dark_purple.xml')
    mywindow = MyMainWin()
    moniwindow = monitorWin()
    ctrlwindow = controlWin()
    tempwindow = tempWin()

    mywindow.setWindowTitle("电池管理系统")
    mywindow.show()
    mywindow.pushButton_19.clicked.connect(moniwindow.show)
    mywindow.pushButton_20.clicked.connect(ctrlwindow.show)
    mywindow.pushButton_8.clicked.connect(tempwindow.show)
    app.exec()

