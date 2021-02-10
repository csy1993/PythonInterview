'''
@Author: CSY
@Date: 2020-02-07 17:39:01
@LastEditors  : CSY
@LastEditTime : 2020-02-07 18:39:07
'''
"""
62、简述cookie和session的区别
"""
# 1，session 在服务器端，cookie 在客户端（浏览器）
# 2、session 的运行依赖 session id，而 session id 是存在 cookie 中的，也就是说，如果浏览器禁用了 cookie ，
# 同时 session 也会失效，存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置
# 3、cookie安全性比session差

