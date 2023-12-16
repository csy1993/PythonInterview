'''
@Author: CSY
@Date: 2020-02-06 16:26:47
@LastEditors  : CSY
@LastEditTime : 2020-02-06 16:27:51
'''
"""
46、a="hello"和b="你好"编码成bytes类型
"""
a="hello"
b="你好"
print(type(a.encode('utf8')))
print(type(b'b'))