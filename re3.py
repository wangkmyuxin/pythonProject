# 王宇鑫创建的学习代码
import os
import re

ifconfig_result = os.popen('ifconfig '+'ens160').read()

ipv4_address = re.findall(r'inet (\d+\.\d+\.\d+\.\d+)', ifconfig_result)[0]
netmask = re.findall(r'netmask (\d+\.\d+\.\d+\.\d+)', ifconfig_result)[0]
broadcast = re.findall(r'broadcast (\d+\.\d+\.\d+\.\d+)', ifconfig_result)[0]
mac_address = re.findall(r'ether ([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})', \
                         ifconfig_result)[0]

a = 'ipv4_address'
b = 'netmask'
c = 'broadcast'
d = 'mac_address'

print(f'{a:<15s}:{ipv4_address}')
print(f'{b:<15s}:{netmask}')
print(f'{c:<15s}:{broadcast}')
print(f'{d:<15s}:{mac_address}')

ipv4_list = ipv4_address.split('.')
ipv4_list[3] = '2'
ipv4_gateway = '.'.join(ipv4_list)

ping_result = os.popen('ping ' + ipv4_gateway + ' -c 1').read()

re_ping = re.findall(r'1 received', ping_result)

print('\n我们假设网关IP地址最后一位是2，因此网关IP地址为:192.168.56.2\n')
if re_ping:
    print('网关可达！')
else:
    print('网关不可达！')