'''
@Author: CSY
@Date: 2020-02-07 17:30:43
@LastEditors  : CSY
@LastEditTime : 2020-02-07 17:35:25
'''
"""
61、简述同源策略
"""
# 1.协议相同
# 2.域名相同
# 3.端口相同

#  http:www.test.com与https:www.test.com 不同源——协议不同 
#  http:www.test.com与http:www.admin.com 不同源——域名不同 
#  http:www.test.com与http:www.test.com:8081 不同源——端口不同
#  只要不满足其中任意一个要求，就不符合同源策略，就会出现“跨域”