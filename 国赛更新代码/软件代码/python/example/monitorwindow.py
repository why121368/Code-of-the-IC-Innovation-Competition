# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitorwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_monitorWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 904)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(190, 20, 521, 31))
        self.label_21.setStyleSheet("border-color: rgb(85, 255, 255);\n"
"")
        self.label_21.setObjectName("label_21")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 250, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 120, 271, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_3.setStyleSheet("color: rgb(99, 78, 255);")
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout_2.addWidget(self.progressBar_3, 2, 0, 1, 1)
        self.progressBar_5 = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_5.setStyleSheet("color: rgb(99, 78, 255);")
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.gridLayout_2.addWidget(self.progressBar_5, 4, 0, 1, 1)
        self.progressBar_7 = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_7.setStyleSheet("color: rgb(99, 78, 255);")
        self.progressBar_7.setProperty("value", 24)
        self.progressBar_7.setObjectName("progressBar_7")
        self.gridLayout_2.addWidget(self.progressBar_7, 6, 0, 1, 1)
        self.progressBar_6 = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_6.setStyleSheet("color: rgb(99, 78, 255);")
        self.progressBar_6.setProperty("value", 24)
        self.progressBar_6.setObjectName("progressBar_6")
        self.gridLayout_2.addWidget(self.progressBar_6, 5, 0, 1, 1)
        self.progressBar_9 = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_9.setStyleSheet("color: rgb(99, 78, 255);")
        self.progressBar_9.setProperty("value", 24)
        self.progressBar_9.setObjectName("progressBar_9")
        self.gridLayout_2.addWidget(self.progressBar_9, 8, 0, 1, 1)
        self.progressBar_8 = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_8.setStyleSheet("color: rgb(99, 78, 255);")
        self.progressBar_8.setProperty("value", 24)
        self.progressBar_8.setObjectName("progressBar_8")
        self.gridLayout_2.addWidget(self.progressBar_8, 7, 0, 1, 1)
        self.progressBar_111 = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_111.setStyleSheet("background-color: rgb(156, 117, 255);")
        self.progressBar_111.setProperty("value", 24)
        self.progressBar_111.setObjectName("progressBar_111")
        self.gridLayout_2.addWidget(self.progressBar_111, 10, 0, 1, 1)
        self.progressBar_4 = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_4.setStyleSheet("color: rgb(99, 78, 255);")
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.gridLayout_2.addWidget(self.progressBar_4, 3, 0, 1, 1)
        self.progressBar_10 = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_10.setStyleSheet("color: rgb(99, 78, 255);")
        self.progressBar_10.setProperty("value", 24)
        self.progressBar_10.setObjectName("progressBar_10")
        self.gridLayout_2.addWidget(self.progressBar_10, 9, 0, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_2.setStyleSheet("color: rgb(99, 78, 255);")
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_2.addWidget(self.progressBar_2, 1, 0, 1, 1)
        self.progressBar_1 = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_1.setStyleSheet("color: rgb(99, 78, 255);")
        self.progressBar_1.setProperty("value", 24)
        self.progressBar_1.setObjectName("progressBar_1")
        self.gridLayout_2.addWidget(self.progressBar_1, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 120, 51, 381))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.splitter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.splitter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.splitter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.splitter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.splitter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.splitter)
        self.label_11.setObjectName("label_11")
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(380, 120, 51, 391))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.v1_10 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.v1_10.setObjectName("v1_10")
        self.gridLayout_4.addWidget(self.v1_10, 10, 0, 1, 1)
        self.v1_6 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.v1_6.setObjectName("v1_6")
        self.gridLayout_4.addWidget(self.v1_6, 5, 0, 1, 1)
        self.v1_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.v1_2.setObjectName("v1_2")
        self.gridLayout_4.addWidget(self.v1_2, 1, 0, 1, 1)
        self.v1_8 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.v1_8.setObjectName("v1_8")
        self.gridLayout_4.addWidget(self.v1_8, 8, 0, 1, 1)
        self.v1_4 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.v1_4.setObjectName("v1_4")
        self.gridLayout_4.addWidget(self.v1_4, 3, 0, 1, 1)
        self.v1_7 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.v1_7.setObjectName("v1_7")
        self.gridLayout_4.addWidget(self.v1_7, 7, 0, 1, 1)
        self.v1_9 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.v1_9.setObjectName("v1_9")
        self.gridLayout_4.addWidget(self.v1_9, 9, 0, 1, 1)
        self.v1_111 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.v1_111.setObjectName("v1_111")
        self.gridLayout_4.addWidget(self.v1_111, 11, 0, 1, 1)
        self.v1_3 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.v1_3.setObjectName("v1_3")
        self.gridLayout_4.addWidget(self.v1_3, 2, 0, 1, 1)
        self.v1_5 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.v1_5.setObjectName("v1_5")
        self.gridLayout_4.addWidget(self.v1_5, 4, 0, 1, 1)
        self.v1_1 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.v1_1.setObjectName("v1_1")
        self.gridLayout_4.addWidget(self.v1_1, 0, 0, 1, 1)
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(450, 120, 51, 391))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.v2_10 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.v2_10.setObjectName("v2_10")
        self.gridLayout_5.addWidget(self.v2_10, 10, 0, 1, 1)
        self.v2_6 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.v2_6.setObjectName("v2_6")
        self.gridLayout_5.addWidget(self.v2_6, 5, 0, 1, 1)
        self.v2_2 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.v2_2.setObjectName("v2_2")
        self.gridLayout_5.addWidget(self.v2_2, 1, 0, 1, 1)
        self.v2_8 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.v2_8.setObjectName("v2_8")
        self.gridLayout_5.addWidget(self.v2_8, 8, 0, 1, 1)
        self.v2_4 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.v2_4.setObjectName("v2_4")
        self.gridLayout_5.addWidget(self.v2_4, 3, 0, 1, 1)
        self.v2_7 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.v2_7.setObjectName("v2_7")
        self.gridLayout_5.addWidget(self.v2_7, 7, 0, 1, 1)
        self.v2_9 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.v2_9.setObjectName("v2_9")
        self.gridLayout_5.addWidget(self.v2_9, 9, 0, 1, 1)
        self.v2_111 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.v2_111.setObjectName("v2_111")
        self.gridLayout_5.addWidget(self.v2_111, 11, 0, 1, 1)
        self.v2_3 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.v2_3.setObjectName("v2_3")
        self.gridLayout_5.addWidget(self.v2_3, 2, 0, 1, 1)
        self.v2_5 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.v2_5.setObjectName("v2_5")
        self.gridLayout_5.addWidget(self.v2_5, 4, 0, 1, 1)
        self.v2_1 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.v2_1.setObjectName("v2_1")
        self.gridLayout_5.addWidget(self.v2_1, 0, 0, 1, 1)
        self.layoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_6.setGeometry(QtCore.QRect(520, 120, 51, 391))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.v3_10 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.v3_10.setObjectName("v3_10")
        self.gridLayout_6.addWidget(self.v3_10, 10, 0, 1, 1)
        self.v3_6 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.v3_6.setObjectName("v3_6")
        self.gridLayout_6.addWidget(self.v3_6, 5, 0, 1, 1)
        self.v3_2 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.v3_2.setObjectName("v3_2")
        self.gridLayout_6.addWidget(self.v3_2, 1, 0, 1, 1)
        self.v3_8 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.v3_8.setObjectName("v3_8")
        self.gridLayout_6.addWidget(self.v3_8, 8, 0, 1, 1)
        self.v3_4 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.v3_4.setObjectName("v3_4")
        self.gridLayout_6.addWidget(self.v3_4, 3, 0, 1, 1)
        self.v3_7 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.v3_7.setObjectName("v3_7")
        self.gridLayout_6.addWidget(self.v3_7, 7, 0, 1, 1)
        self.v3_9 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.v3_9.setObjectName("v3_9")
        self.gridLayout_6.addWidget(self.v3_9, 9, 0, 1, 1)
        self.v3_111 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.v3_111.setObjectName("v3_111")
        self.gridLayout_6.addWidget(self.v3_111, 11, 0, 1, 1)
        self.v3_3 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.v3_3.setObjectName("v3_3")
        self.gridLayout_6.addWidget(self.v3_3, 2, 0, 1, 1)
        self.v3_5 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.v3_5.setObjectName("v3_5")
        self.gridLayout_6.addWidget(self.v3_5, 4, 0, 1, 1)
        self.v3_1 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.v3_1.setObjectName("v3_1")
        self.gridLayout_6.addWidget(self.v3_1, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(380, 100, 51, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(450, 100, 51, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(520, 100, 51, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(600, 89, 81, 31))
        self.label_15.setObjectName("label_15")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(730, 390, 101, 87))
        self.textEdit.setObjectName("textEdit")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(730, 360, 72, 15))
        self.label_16.setObjectName("label_16")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(730, 180, 101, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(730, 160, 72, 15))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(840, 170, 31, 31))
        self.label_18.setObjectName("label_18")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(730, 120, 101, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(840, 110, 31, 31))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(730, 100, 72, 15))
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(100, 80, 281, 31))
        self.label_22.setStyleSheet("border-color: rgb(85, 255, 255);\n"
"")
        self.label_22.setObjectName("label_22")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 891, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(730, 300, 101, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 500, 901, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(730, 10, 101, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(680, 70, 41, 461))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(510, 530, 121, 351))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(590, 120, 95, 381))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout.addWidget(self.pushButton_12)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(590, 640, 121, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(590, 760, 121, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(110, 550, 281, 31))
        self.label_23.setStyleSheet("border-color: rgb(85, 255, 255);\n"
"")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(510, 550, 281, 31))
        self.label_24.setStyleSheet("border-color: rgb(85, 255, 255);\n"
"")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(20, 780, 51, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(220, 780, 51, 16))
        self.label_26.setObjectName("label_26")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 780, 51, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 780, 51, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(430, 660, 101, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(430, 580, 72, 15))
        self.label_27.setObjectName("label_27")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(430, 600, 101, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(430, 640, 72, 15))
        self.label_28.setObjectName("label_28")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(430, 730, 101, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(430, 770, 101, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(130, 770, 31, 31))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(330, 770, 31, 31))
        self.label_30.setObjectName("label_30")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(750, 770, 101, 31))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(750, 730, 101, 31))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(750, 580, 72, 15))
        self.label_31.setObjectName("label_31")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(750, 660, 101, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(750, 600, 101, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(750, 640, 72, 15))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(590, 610, 51, 16))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(590, 730, 51, 16))
        self.label_34.setObjectName("label_34")
        self.widget_2 = AnalogGaugeWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 600, 171, 161))
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = AnalogGaugeWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(200, 600, 181, 161))
        self.widget_3.setObjectName("widget_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">监测功能界面</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "单次功能测试"))
        self.label.setText(_translate("MainWindow", "电池1"))
        self.label_2.setText(_translate("MainWindow", "电池2"))
        self.label_3.setText(_translate("MainWindow", "电池3"))
        self.label_4.setText(_translate("MainWindow", "电池4"))
        self.label_5.setText(_translate("MainWindow", "电池5"))
        self.label_6.setText(_translate("MainWindow", "电池6"))
        self.label_7.setText(_translate("MainWindow", "电池7"))
        self.label_8.setText(_translate("MainWindow", "电池8"))
        self.label_9.setText(_translate("MainWindow", "电池9"))
        self.label_10.setText(_translate("MainWindow", "电池10"))
        self.label_11.setText(_translate("MainWindow", "总电池"))
        self.v1_1.setToolTip(_translate("MainWindow", "<html><head/><body><p>电池1</p></body></html>"))
        self.v2_1.setToolTip(_translate("MainWindow", "<html><head/><body><p>电池1</p></body></html>"))
        self.v3_1.setToolTip(_translate("MainWindow", "<html><head/><body><p>电池1</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "真实值"))
        self.label_13.setText(_translate("MainWindow", "监测值"))
        self.label_14.setText(_translate("MainWindow", "误差值"))
        self.label_15.setText(_translate("MainWindow", "ADC异常"))
        self.label_16.setText(_translate("MainWindow", "测试结果"))
        self.label_17.setText(_translate("MainWindow", "误差阈值"))
        self.label_18.setText(_translate("MainWindow", "mV"))
        self.label_19.setText(_translate("MainWindow", "V"))
        self.label_20.setText(_translate("MainWindow", "参考电压"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">电压检测功能</span></p></body></html>"))
        self.pushButton_13.setText(_translate("MainWindow", "保存测试结果"))
        self.pushButton_14.setText(_translate("MainWindow", "生成测试报告"))
        self.pushButton_2.setText(_translate("MainWindow", "ADC1"))
        self.pushButton_3.setText(_translate("MainWindow", "ADC2"))
        self.pushButton_4.setText(_translate("MainWindow", "ADC3"))
        self.pushButton_5.setText(_translate("MainWindow", "ADC4"))
        self.pushButton_6.setText(_translate("MainWindow", "ADC5"))
        self.pushButton_7.setText(_translate("MainWindow", "ADC6"))
        self.pushButton_8.setText(_translate("MainWindow", "ADC7"))
        self.pushButton_9.setText(_translate("MainWindow", "ADC8"))
        self.pushButton_10.setText(_translate("MainWindow", "ADC9"))
        self.pushButton_11.setText(_translate("MainWindow", "ADC10"))
        self.pushButton_12.setText(_translate("MainWindow", "ADC0"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">电流检测功能</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">温度检测功能</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "真实值"))
        self.label_26.setText(_translate("MainWindow", "检测值"))
        self.label_27.setText(_translate("MainWindow", "误差值"))
        self.label_28.setText(_translate("MainWindow", "误差阈值"))
        self.pushButton_15.setText(_translate("MainWindow", "单次功能测试"))
        self.pushButton_16.setText(_translate("MainWindow", "保存测试结果"))
        self.label_29.setText(_translate("MainWindow", "mA"))
        self.label_30.setText(_translate("MainWindow", "mA"))
        self.pushButton_17.setText(_translate("MainWindow", "保存测试结果"))
        self.pushButton_18.setText(_translate("MainWindow", "单次功能测试"))
        self.label_31.setText(_translate("MainWindow", "误差值"))
        self.label_32.setText(_translate("MainWindow", "误差阈值"))
        self.label_33.setText(_translate("MainWindow", "真实值"))
        self.label_34.setText(_translate("MainWindow", "检测值"))
        self.menu.setTitle(_translate("MainWindow", "监测功能界面"))

        self.widget_2.setGaugeTheme(7)
        self.widget_2.units = "mA"
        self.widget_3.setGaugeTheme(7)
        self.widget_3.units = "mA"

        self.progressBar_1.setRange(0, 200)
        self.progressBar_2.setRange(0, 200)
        self.progressBar_3.setRange(0, 200)
        self.progressBar_4.setRange(0, 200)
        self.progressBar_5.setRange(0, 200)
        self.progressBar_6.setRange(0, 200)
        self.progressBar_7.setRange(0, 200)
        self.progressBar_8.setRange(0, 200)
        self.progressBar_9.setRange(0, 200)
        self.progressBar_10.setRange(0, 200)
        self.progressBar_111.setRange(0, 200)
from analoggaugewidget import AnalogGaugeWidget
