# 王宇鑫创建的学习代码
import paramiko
import re
import hashlib
import time

def device_ssh(ip,username,password,cmd_list,enable='',wait_time=2,verbose=True):
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
    return x
        # if verbose:
        #     print(x)
    chan.close()
    ssh.close()

def get_config(ip,username,password):
    try:
        device_config_raw = device_ssh(ip, username, password,['terminal length 0','show run'])
        result = re.split(r'\r\nhostname \S+\r\n',device_config_raw)
        config = device_config_raw.replace(result[0],'').strip()
        return config
    except Exception:
        return

def get_check_md5(ip,username,password):
    before_md5 = ''
    while True:
        get_deviceconfig = get_config(ip, username, password)
        m = hashlib.md5()
        m.update(get_deviceconfig.encode())
        md5_value = m.hexdigest()
        print(md5_value)
        if not before_md5:
            before_md5 = md5_value
        elif before_md5 != md5_value:
            print('MD5 值改变了')
            break
        time.sleep(5)


if __name__ == '__main__':
    # print(get_config('192.168.56.130','wangyuxin','2016'))
    get_check_md5('192.168.56.130', 'wangyuxin', '2016')
    # print(device_ssh('192.168.56.130','wangyuxin','2016',['terminal length 0','show run']))
