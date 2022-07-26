# 王宇鑫创建的学习代码
from ssh1 import linux_ssh
from argparse import ArgumentParser

usage = "usage:python ssh_module -i ipaddr -u username -p password -c command"

parser = ArgumentParser(usage=usage)

parser.add_argument("-i", "--ipaddr", dest="ipaddr", help="SSH Server", default="192.168.56.130", type=str)
parser.add_argument("-u", "--username", dest="username", help="SSH Username", default="wangyuxin", type=str)
parser.add_argument("-p", "--password", dest="password", help="SSH Password", default="2016", type=str)
parser.add_argument("-c", "--command", dest="command", help="Shell Command", default="show ip int bri", type=str)
a = parser.parse_args()

print(linux_ssh(a.ipaddr, a.username, a.password, cmd=a.command))
