'''
@Author: CSY
@Date: 2020-02-06 14:54:46
@LastEditors  : CSY
@LastEditTime : 2020-02-06 15:45:04
'''
"""
41、举例说明异常模块中try except else finally的相关意义
"""
try:
    print(1)
    a=1/0
    print(2)
except:
    print("出现错误")
else:
    print("没出错")
finally:
    print("有没有错都要执行")