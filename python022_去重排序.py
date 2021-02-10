'''
@Author: CSY
@Date: 2020-01-25 12:56:06
@LastEditors  : CSY
@LastEditTime : 2020-01-25 13:15:41
'''
"""
22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
"""
s="ajldjlajfdljfddd"
set_s=set(s)
print(set_s)
list_s=list(set_s)
print(list_s)
list_s.sort()
print(list_s)