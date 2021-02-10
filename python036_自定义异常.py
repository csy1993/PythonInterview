'''
@Author: CSY
@Date: 2020-02-04 17:30:09
@LastEditors  : CSY
@LastEditTime : 2020-02-04 17:31:49
'''
"""
36、写一段自定义异常代码
"""
def error_test():
    try:
        for i in range(1,5):
            if i > 2:
                raise Exception("数字过大")
            print(i)
    except Exception as e:
        print(e)
error_test()