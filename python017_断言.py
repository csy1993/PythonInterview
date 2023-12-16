'''
@Author: CSY
@Date: 2020-01-17 20:12:56
@LastEditors  : CSY
@LastEditTime : 2020-01-17 20:14:04
'''
"""
17、python中断言方法举例
"""
a=10
assert(a>1)
print("断言成功")
try:
    assert(a<1)
except:
    print("断言失败")