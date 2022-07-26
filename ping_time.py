# 王宇鑫创建的学习代码
from datetime import datetime
from datetime import timedelta

now = datetime.now()
five_days = now - timedelta(days=5)
file_name = 'save_fivedayago_time_' + now.strftime("%Y-%m-%d_%H-%M-%S") + '.txt'
file = open(file_name, 'w')
file.write(str(now))
file.close()