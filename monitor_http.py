# 王宇鑫创建的学习代码
# -*- coding=utf-8 -*-

import os
import re
import time

while True:
    http_status = os.popen('netstat -ntlp').read()
    http_find = re.findall(r'(tcp).*0.0.0.0:(8080).*', http_status)
    if http_find == []:
        time.sleep(1)
        print('等待一秒重新开始监控！')
    elif http_find[0][1] =='8080':
        print('HTTP(TCP/8080)服务已经被打开')
        break




