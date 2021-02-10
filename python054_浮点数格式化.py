'''
@Author: CSY
@Date: 2020-02-07 14:45:53
@LastEditors  : CSY
@LastEditTime : 2020-02-07 14:49:14
'''
"""
54、保留两位小数
题目本身只有a="%.03f"%1.3335,让计算a的结果，为了扩充保留小数的思路，提供round方法（数值，保留位数）
"""
a="%.03f"%1.3335
print(a,type(a))
print(float(a))
print(round(float(a),1))