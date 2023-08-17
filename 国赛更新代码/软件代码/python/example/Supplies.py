# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:58:27 2023

@author: jackscl
"""

import matplotlib.pyplot as plt
import numpy as np
import time
import sys,os
import pathlib
py_path, py_name = os.path.split(os.path.abspath(__file__))

base_dir = pathlib.Path(py_path).absolute().parent  # sys.argv[0]

if sys.path.count(base_dir) == 0:
    sys.path.append(str(base_dir))
from pyRD import RD
from pyRD.core.RDconstant import *
def fan():
    rd=RD()
    rd.DeviceEnumLists()
    rd.DeviceOpen(0)
    #Supplies
    postivech=0
    posV=5.0

    rd.AnalogIOChannelNodeSet(postivech,posV)
    rd.AnalogIOChannelEnableSet(postivech,1)
    return rd


def not_fan(rd):
    # py_path, py_name = os.path.split(os.path.abspath(__file__))
    #
    # base_dir = pathlib.Path(py_path).absolute().parent  # sys.argv[0]
    #
    # if sys.path.count(base_dir) == 0:
    #     sys.path.append(str(base_dir))
    rd.DeviceEnumLists()
    rd.DeviceOpen(0)
    postivech=0
    # close connect
    rd.AnalogIOChannelEnableSet(postivech,0)
    # close connect
    # print(rd.DeviceClose())

rd = fan()
not_fan(rd)