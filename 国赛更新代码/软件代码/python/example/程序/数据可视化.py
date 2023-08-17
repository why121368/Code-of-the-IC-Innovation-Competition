from fpdf import FPDF

def report():
    ch = 8
    class PDF(FPDF):
        def __init__(self):
            super().__init__()
        def header(self):
            self.set_font('song', '', 12)
            self.cell(0, 10, '电池管理芯片BQ76930', 0, 1, 'C')
        def footer(self):
            self.set_y(-15)
            self.set_font('song', '', 12)
            self.cell(0, 8, f'Page {self.page_no()}', 0, 0, 'C')
    pdf = PDF()
    pdf.add_font('song','','song.ttf',True)
    pdf.add_page()
    pdf.set_fill_color(248,245,235)
    pdf.set_font("song", '',24)
    pdf.cell(w=0, h=20, txt="电池管理芯片测试报告", ln=1)
    pdf.set_font("song", '',16)
    pdf.cell(w=30, h=ch, txt="时间: ", ln=0)
    pdf.cell(w=30, h=ch, txt="07/15/2023", ln=1)
    pdf.cell(w=30, h=ch, txt="测试设备: ", ln=0)
    pdf.cell(w=30, h=ch, txt="雨珠测试系统", ln=1)
    pdf.ln(ch)
    pdf.multi_cell(w=0, h=7, txt='  本测试系统为雨珠测试系统，经过对芯片的检测功能和保护功能的测试，系统将数据整理如下，以供测试人员参考')

    txt = '芯片电压测试功能正常,所有ADC测试值均在误差范围内。'
    txt2 = '芯片电流测试功能正常，测试值误差小于误差阈值。'
    txt3 = '芯片温度测试功能正常，测试值小于误差阈值'


    pdf.ln(ch)
    pdf.set_font("song", '',20)
    pdf.multi_cell(w=0, h=10, txt='一.电压检测功能')

    pdf.set_font("song", '',16)
    pdf.multi_cell(w=0, h=7, txt='电压监测功能的对象是被管理电池组的总电压和10节电池的单体电压，使用测试系统的单次测试模式或连续测试模式均可以对此功能进行测试。将输出电压为12.0V电压源的正负极分别与测试板的BAT+、BAT-相连，并使用万用表对于各电池的单体电压进行测量测试系统通过对电压测试结果：'+ txt +'ADC测量值与真实值统计分析如下:'+'       ')
    pdf.image('voltage.png',
              x = 10, y = None, w = 190, h = 80, type = 'PNG')
    pdf.multi_cell(w=0, h=7, txt='       '+'分析可知，测试系统采集的电压监测功能测试数据和万用表测量的数据之间，存在着25mV左右的差值,此差值对应了芯片工作温度在0℃至60℃的之间时，ADC在进行电池组电压采样时存在的±25mV的采样误差。测试结果表明，系统可以对待测芯片的电压监测功能和ADC采样误差进行有效测试，系统数据误差最大为4mV，满足了5mV以内系统误差的性能指标。')

    pdf.ln(ch)
    pdf.set_font("song", '',20)
    pdf.multi_cell(w=0, h=10, txt='二.电流检测功能')

    pdf.set_font("song", '',16)
    pdf.multi_cell(w=0, h=7, txt='  电流测试结果：'+ txt +'CC测量值与真实值统计分析如下:')
    pdf.image('current.png',
              x = 32, y = None, w = 150, h = 90, type = 'PNG')

    pdf.ln(ch)
    pdf.set_font("song", '',20)
    pdf.multi_cell(w=0, h=10, txt='三.温度检测功能')

    pdf.set_font("song", '',16)
    pdf.multi_cell(w=0, h=7, txt='  温度测试结果：'+ txt +'CC测量值与真实值统计分析如下:')
    pdf.image('wendu.png',
              x = 32, y = None, w = 150, h = 90, type = 'PNG')

    pdf.output(f'./example.pdf', 'F')

report()