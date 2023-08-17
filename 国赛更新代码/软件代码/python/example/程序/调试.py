        self.widget.setGaugeTheme(7)
        self.widget.maxValue = 10
        self.widget.units = "mA"
        self.widget_2.setGaugeTheme(8)
        self.widget_2.maxValue = 100
        self.widget_2.units = "C"


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

        now_date = time.strftime("%Y-%m-%d", time.localtime())

        self.lineEdit_12.setText('192.168.137.103')
        self.lineEdit_13.setText('BQ76930')
        self.lineEdit_14.setText('100KHZ')
        self.time.setText(str(now_date))
from analoggaugewidget import AnalogGaugeWidget