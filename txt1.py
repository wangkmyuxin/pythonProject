# 王宇鑫创建的学习代码

import os

os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1','w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2','w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3','w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')

txt = []
for file in os.listdir(os.getcwd()):
    if os.path.isdir(file):
        os.chdir(file)
        for i in os.listdir(os.getcwd()):
            if os.path.isfile(i):
                for file_read in open(i):
                    if 'qytang' in file_read:
                        txt.append(i)

print('文件中包含"qytang"关键字的文件为：')
for txt in txt:
    print(txt)

os.chdir('..')
for root, dirs, files in os.walk('/pythonproject/test', topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
os.removedirs('/pythonproject/test')
