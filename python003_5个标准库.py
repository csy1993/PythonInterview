'''
@Author: CSY
@Date: 2019-12-09 20:37:03
@LastEditors: CSY
@LastEditTime: 2019-12-09 20:40:46
'''
"""
3、列出5个python标准库
"""
# 1.os:提供操作系统相关函数
import os
print(os.environ)

# 2.sys:命令行参数
import sys
print(sys.path)

# 3.re:正则
import re
print(re.compile('^c'))

# 4.math:数学表达式
import math
print(math.pi)

# 5.time:时间相关
import time
print(time.time())