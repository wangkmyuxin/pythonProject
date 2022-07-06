# 王宇鑫创建的学习代码

import os
import re

route_n_result = os.popen('route -n').read()
Gateway = re.findall('0.0.0.0\s+(\d+\.\d+\.\d+\.\d)+.*(UG)',route_n_result)
print('网关为:', Gateway[0][0])