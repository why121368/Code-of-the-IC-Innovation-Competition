import paramiko
import dataprocessing as proc
# 输入用户名、密码、ip等

ip = "192.168.137.197"
port = 22
user = "pi"
password = "raspberry"
# 创建一个ssh对象
ssh = paramiko.SSHClient()
# 自动选择yes
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 建立连接
ssh.connect(ip, port, user, password, timeout=10)

#temp = 'sudo i2cdetect -y -a 1'
temp = 'sudo i2cget -y -f 1 0x08 0x00'
stdin, stdout, stderr = ssh.exec_command(temp)
# 输出命令执行结果
result = stdout.read()

def pre(m):
    w = ['']*4
    re = ['']*2
    n = 0
    x = 0
    for i in m:
        if n == 1:
            w[x] = i
            x += 1
        if i == 'x':
            n = 1
        if i == 'n':
            n = 0
    re[0] = w[0]
    re[1] = w[1]
    return re

#传入字符串地址
def read(address):
    tmp = 'sudo i2cget -y -f 1 0x08 ' + address
    stdin,stdout,stderr = ssh.exec_command(tmp)
    # 输出命令执行结果
    result = stdout.read()
    result = pre(str(result))
    result = proc.trans(result[0]) + proc.trans(result[1])
    return result

#传入字符串地址和数据
def write(address,data):
    tmp = 'sudo i2cset -y -f 1 0x08 ' + address +' '+ data
    stdin, stdout, stderr = ssh.exec_command(tmp)
    # 输出命令执行结果
    result = stdout.read()
    return result
#
# write('0x06','0x9f')
# x1 = read('0x06')

# print(x1)

