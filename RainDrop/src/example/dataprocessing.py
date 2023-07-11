import pandas as pd

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


