'''
@Author: CSY
@Date: 2020-02-07 16:48:33
@LastEditors  : CSY
@LastEditTime : 2020-02-07 16:49:14
'''
"""
58、使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
"""
dict01={"name":"zs","age":18}
dict01.pop("name")
print(dict01)
del dict01['age']
print(dict01)