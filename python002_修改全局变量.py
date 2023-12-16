'''
@Author: CSY
@Date: 2019-12-09 20:35:06
@LastEditors: CSY
@LastEditTime: 2019-12-09 20:36:25
'''
"""
2、如何在一个函数内部修改全局变量
"""
def demo():
    global a
    a=10

demo()
print(a)