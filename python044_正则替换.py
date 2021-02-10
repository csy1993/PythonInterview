'''
@Author: CSY
@Date: 2020-02-06 15:58:12
@LastEditors  : CSY
@LastEditTime : 2020-02-06 16:14:06
'''
"""
44、a="张明 98分"，用re.sub，将98替换为100
"""
import re
a="张明 98分"
print(re.sub(r'98','100',a))
