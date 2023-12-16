'''
@Author: CSY
@Date: 2020-01-28 11:42:44
@LastEditors  : CSY
@LastEditTime : 2020-01-28 11:57:27
'''
"""
28、列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list01=[x for x in a if x%2==1]
print(list01)