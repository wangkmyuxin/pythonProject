# 王宇鑫创建的学习代码
# 制作一个能执行多条命令（配置路由器）的函数，参数设计如下:
# def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
# cmd_list: 传入一个执行命令的清单
# enable: 解决可能有enable密码的情况！如果没有enable密码就保持为''(空)，如果有enable密码就传输enable密码
# wait_time: 控制等待网络设备返回信息的时间
# verbose: 决定是否打印网络设备返回信息, True为打印， False为不打印

import paramiko
import time

def ssh_module(ip,username,password,cmd_list,enable='',wait_time=2,verbose=True):
    ssh = paramiko.SSHClient() # 创建SSH Client
    ssh.load_system_host_keys() # 加载系统SSH密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 添加新的SSH密钥
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)  # SSH连接
    chan = ssh.invoke_shell()  # 激活交互式shell
    time.sleep(1)  # 等待网络设备回应
    x = chan.recv(2048).decode()  # 获取路由器返回的信息
    if enable and '>' in x:
        chan.send('enable'.encode())  # 发送命令
        chan.send(b'\n')  # 回车
        chan.send(enable.encode())
        chan.send(b'\n')  # 回车
        time.sleep(wait_time)
    elif not enable and '>' in x:
        print('需要配置enable 密码')
        retrun
    for cmd in cmd_list:
        chan.send(cmd.encode())  # 发送命令
        chan.send(b'\n')  # 回车
        time.sleep(wait_time)
        x = chan.recv(40960).decode()
        if verbose:
            print(x)
    chan.close()
    ssh.close()

if __name__ == '__main__':
    ssh_module('192.168.56.130',
               'wangyuxin',
                '2016',
               ['terminal length 0',
                'show version',
                'config terminal',
                'router ospf 1',
                'network 192.168.56.130 0.0.0.255 area 0'],
               enable='2016',
               wait_time=1,
               verbose=True)
