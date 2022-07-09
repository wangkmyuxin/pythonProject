# 王宇鑫创建的学习代码
import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n\
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}

for i in asa_conn.split('\n'):
    re_result = re.match('\w+\s+\w+\s+(\d+\.\d+\.\d+\.\d+):(\d+)\s+\w+\s+(\d+\.\d+\.\d+\.\d+):(\d+),\s+\w+\s+.*\s+(\d+),\s+\w+\s+(\w+)', \
                         i).groups()
    asa_dict[re_result[0:4]] = re_result[4:6]
print('\n打印分析后的字典！\n')
print(asa_dict)

src_ip = 'src_ip'
src_prot = 'src_prot'
des_ip = 'des_ip'
des_port ='des_port'
bytes_name ='bytes'
flags = 'flags'

print('\n格式化打印输出！\n')
for key, value in asa_dict.items():
    print(f'{src_ip:^15s}:{key[0]:^15s} | {src_prot:^15s}:{key[1]:^15s} | {des_ip:^15s}:{key[2]:^15s} | {des_port:^15s}:{key[3]:^15s}')
    print(f'{bytes_name:^15s}:{value[0]:^15s} | {flags :^15s}:{value[1]:^15s} ')
    print('='*130)

