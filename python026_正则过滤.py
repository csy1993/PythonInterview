'''
@Author: CSY
@Date: 2020-01-27 20:34:19
@LastEditors  : CSY
@LastEditTime : 2020-01-28 09:49:51
'''
"""
26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"
"""
import re
a = "not 404 found 张三 99 深圳"
list01=a.split(' ')
print(list01)
res=re.findall(r'\d+|[a-zA-Z]+',a)
print(res)
for i in res:
    # print(i)
    if i in list01:
        list01.remove(i)
print(list01)
