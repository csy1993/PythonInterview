'''
@Author: CSY
@Date: 2020-02-08 16:06:42
@LastEditors  : CSY
@LastEditTime : 2020-02-08 16:54:08
'''
"""
72、对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
"""
list01 = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
list02=sorted(list01,key=lambda x:x)
print(list02)