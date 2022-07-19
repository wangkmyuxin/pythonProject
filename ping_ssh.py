# 王宇鑫创建的学习代码

from ping import wyx_ping
from ssh1 import linux_ssh
import re
import pprint

def wyx_get_router(*ips,username='wangyuxin',password='2016'):
    device_get_dict = {}
    for ip in ips:
        get_dict = {}
        if wyx_ping(ip):
            for i in linux_ssh(ip,username,password,cmd='show ip int bri').split('\n'):
                re_result = re.match(f'(\w+\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+\s+\w+\s+\w+',i)
                if re_result:
                    get_dict[re_result.groups()[0]] = re_result.groups()[1]
        device_get_dict[ip] = get_dict
    return device_get_dict

if __name__ == '__main__':
    pprint.pprint(wyx_get_router('192.168.56.130','192.168.56.200',username='wangyuxin',password='2016'),indent=4)