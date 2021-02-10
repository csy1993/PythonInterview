'''
@Author: CSY
@Date: 2020-01-27 15:42:37
@LastEditors  : CSY
@LastEditTime : 2020-01-27 16:05:57
'''
"""
24、字典根据键从小到大排序
"""
dict01={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

for i in sorted(dict01):
    print(i,dict01[i])
