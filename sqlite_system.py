# 王宇鑫创建的学习代码
import sqlite3
import os

# Python字典对象，我们将把它写入sqlite数据库
homework_dict = [{'姓名': '学员1', '年龄': 37, '作业数': 1},
                 {'姓名': '学员2', '年龄': 33, '作业数': 5},
                 {'姓名': '学员3', '年龄': 32, '作业数': 10}]

# 连接sqlite数据库
if os.path.exists('homework.sqlite'):
    os.remove('homework.sqlite')

conn = sqlite3.connect('homework.sqlite')
cursor = conn.cursor()

# 执行创建表的任务
cursor.execute("create table homework_info (姓名 varchar(40), 年龄 int, 作业数 int)")

# 读取Python字典数据，并逐条写入sqlite数据库
for s in homework_dict:
    name = s['姓名']
    age = s['年龄']
    homework = s['作业数']
    cursor.execute("insert into homework_info values (?,?,?)",(name, age, homework))

conn.commit()