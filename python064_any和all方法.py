'''
@Author: CSY
@Date: 2020-02-07 18:43:09
@LastEditors  : CSY
@LastEditTime : 2020-02-07 19:28:09
'''
"""
64、简述any()和all()方法
"""
# any:任意满足
# all:全部满足

# python中什么元素为假？
# 答案：（0，空字符串，空列表、空字典、空元组、None, False）

print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(None))
print(bool(False))

a=([],'b')
print(any(a))
print(all(a))