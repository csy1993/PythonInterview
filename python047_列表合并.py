'''
@Author: CSY
@Date: 2020-02-06 16:39:12
@LastEditors  : CSY
@LastEditTime : 2020-02-06 16:40:10
'''
"""
47、[1,2,3]+[4,5,6]的结果是多少？
"""
a=[1,2,3]
b=[4,5,6]
print(a+b)
a.extend(b)
print(a)