'''
@Author: CSY
@Date: 2020-02-06 19:12:49
@LastEditors  : CSY
@LastEditTime : 2020-02-07 14:45:14
'''
"""
53、写一个单列模式
"""
class Test01(object):
    __instance=None
    def __new__(cls,age,name):
        if not cls.__instance:
            cls.__instance=object.__new__(cls)
        return cls.__instance

a=Test01(11,'a')
b=Test01(12,'b')

print(id(a))
print(id(b))
