'''
@Author: CSY
@Date: 2020-01-28 09:50:50
@LastEditors  : CSY
@LastEditTime : 2020-01-28 09:53:50
'''
"""
27、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fn(x):
    return x%2==1

list01=filter(fn,a)
print(list01)
for i in list01:
    print(i)