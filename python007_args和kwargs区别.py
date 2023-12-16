'''
@Author: CSY
@Date: 2019-12-09 21:19:27
@LastEditors: CSY
@LastEditTime: 2019-12-09 21:28:32
'''
"""
7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
"""
# args接收不定长列表
def args_demo(*args):
    print(args)

args_demo(1,2)


# kwargs接收不定长字典
def kwargs_demo(**kwargs):
    print(kwargs)

kwargs_demo(name='csy')
