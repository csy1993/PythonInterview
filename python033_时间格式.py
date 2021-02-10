'''
@Author: CSY
@Date: 2020-02-04 16:44:33
@LastEditors  : CSY
@LastEditTime : 2020-02-04 16:46:50
'''
"""
33、log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
"""
import datetime
log01=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(log01)