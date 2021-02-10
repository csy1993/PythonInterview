'''
@Author: CSY
@Date: 2020-01-13 20:50:57
@LastEditors  : CSY
@LastEditTime : 2020-01-13 21:06:26
'''
"""
13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
"""
list01=[1,2,3,4,5]

def square(x):
    return x*x

list02=map(square,list01)
print(list02)

list03=[j for j in list02 if j>10]
print(list03)