'''
@Author: CSY
@Date: 2020-02-06 18:39:57
@LastEditors  : CSY
@LastEditTime : 2020-02-06 19:01:41
'''
"""
52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
"""
list01=[2,3,5,4,9,6]
list02=[]
while len(list01)>0:
    min_num=min(list01)
    # print(min_num)
    list01.remove(min_num)
    # print(list01)
    list02.append(min_num)
    # print(list02)
print(list02)