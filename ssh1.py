# 王宇鑫创建的学习代码

import paramiko
import os
import re

def linux_ssh(ip,username,password,port=22,cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

def ssh_get_gateway(ip,username,password,port=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    route_n_result = os.popen('route -n').read()
    Gateway = re.findall('0.0.0.0\s+(\d+\.\d+\.\d+\.\d)+.*(UG)', route_n_result)
    y = Gateway[0][0]
    return y

if __name__ == '__main__':
    print(linux_ssh('192.168.122.1', 'root', '2016@cisco.com'))
    print(linux_ssh('192.168.122.1', 'root', '2016@cisco.com', cmd='pwd'))
    print('网关为:')
    print(ssh_get_gateway('192.168.122.1', 'root', '2016@cisco.com'))
