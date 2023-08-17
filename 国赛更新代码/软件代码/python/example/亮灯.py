import time


def dianya():
    rd = RD()
    rd.DeviceEnumLists()
    print(rd.devicelist)
    print(rd.DeviceOpen(0))
    # Supplies
    CHs_OUT = 0b1111111111111111  # DIO0 enable output
    CHs_OUTValue = 0b1111111111111111  # DIO0 output value set high

    rd.DigitalIOOutputEnableSet(CHs_OUT)
    rd.DigitalIOOutputSet(CHs_OUTValue)
    rd.DigitalIOInputStatus()  # first reading drop
    py_path, py_name = os.path.split(os.path.abspath(__file__))

    base_dir = pathlib.Path(py_path).absolute().parent  # sys.argv[0]
    time.sleep(10)



    # # close all instruments
    # rd.AnalogInRun(False)
    # # close connect
    # rd.DeviceClose()
    return value