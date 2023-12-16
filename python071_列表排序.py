'''
@Author: CSY
@Date: 2020-02-08 15:44:41
@LastEditors  : CSY
@LastEditTime : 2020-02-08 16:05:57
'''
"""
71、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
"""
list01=[0,-1,3,-10,5,9]
list01.sort()
print(f"sort函数在原基础上修改，无返回值  {list01}")
print(f"sorted返回新列表  {sorted(list01)}")