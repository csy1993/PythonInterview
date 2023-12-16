'''
@Author: CSY
@Date: 2020-02-04 18:47:31
@LastEditors  : CSY
@LastEditTime : 2020-02-04 18:58:38
'''
"""
39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
"""
list01=[[1,2],[3,4],[5,6]]
# 先将list01中的数据给i，再把i给j
list02=[j for i in list01 for j in i]
print(list02)