# 王宇鑫创建的学习代码
import re

a = input()
b = a.split(' ')
for i in b:
    if 'Y' in i:
        c = b.index(i)
        d = b[c-1]+b[c]
        # e = re.match('(\d+)/[N|Y](\d+)/[N|Y]',d).groups()
        e = re.match('(\w+)/\w+(\d+)/\w+',d).groups()
        print(e[0], e[1])




