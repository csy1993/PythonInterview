'''
@Author: CSY
@Date: 2019-12-09 20:40:57
@LastEditors: CSY
@LastEditTime: 2019-12-09 20:48:20
'''
"""
4、字典如何删除键和合并两个字典
"""
dict01={
    "name":"csy",
    "age":28
}
del dict01['age']
print(dict01)

dict02={
    "hobby":"games"
}

dict01.update(dict02)
print(dict01)