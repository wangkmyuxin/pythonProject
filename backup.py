# 王宇鑫创建的学习代码
import paramiko
import re
import hashlib
import time
import sqlite3
from md5 import device_ssh

def get_config(ip,username,password):
    try:
        device_config_raw = device_ssh(ip, username, password,['terminal length 0','show run'])
        result = re.split(r'\r\nhostname \S+\r\n',device_config_raw)
        config = device_config_raw.replace(result[0],'').strip()
        m = hashlib.md5()
        m.update(config.encode())
        md5_value = m.hexdigest()
        return config, md5_value
    except Exception:
        return

device_list = ['192.168.56.130']
username = 'wangyuxin'
password = '2016'

def write_config_md5_db():
    conn = sqlite3.connect('backupconfig.sqlite')
    cursor = conn.cursor()
    for device in device_list:
        config_and_md5 = get_config(device, username, password)
        cursor.execute('select * from config_md5 where ip=?', (device,))
        md5_result = cursor.fetchall()           #返回格式[()]
        if not md5_result:
            cursor.execute('insert into config_md5(ip,config,md5) values (?,?,?)',(device,
                                                                                  config_and_md5[0],
                                                                                  config_and_md5[1]))
            conn.commit()
        else:
            if config_and_md5[1] != md5_result[0][2]:
                cursor.execute('update config_md5 set config=?,md5=? where ip=?',(config_and_md5[0],
                                                                                  config_and_md5[1],
                                                                                  device))
                conn.commit()
            else:
                continue
    cursor.execute('select * from config_md5')
    f_result = cursor.fetchall()
    for i in f_result:
        print(i[0],i[2])
    conn.close()

if __name__ == '__main__':
    # import os
    # if os.path.exists('backupconfig.sqlite'):
    #     os.remove('backupconfig.sqlite')
    #
    # conn = sqlite3.connect('backupconfig.sqlite')
    # cursor = conn.cursor()
    #
    # # 执行创建表的任务
    # cursor.execute("create table config_md5 (ip varchar(40), config varchar(99999), md5 varchar(1000))")
    # conn.commit()
    # conn.close()
    # print(get_config('192.168.56.130', 'wangyuxin', '2016'))
    write_config_md5_db()
