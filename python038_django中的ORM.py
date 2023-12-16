'''
@Author: CSY
@Date: 2020-02-04 18:45:56
@LastEditors  : CSY
@LastEditTime : 2020-02-04 18:47:02
'''
"""
38、简述Django的orm
"""
# ORM，全拼Object-Relation Mapping，意为对象-关系映射
# 实现了数据模型与数据库的解耦，通过简单的配置就可以轻松更换数据库，而不需要修改代码只需要面向对象编程,
# orm操作本质上会根据对接的数据库引擎，翻译成对应的sql语句,
# 所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite....，如果数据库迁移，只需要更换Django的数据库引擎即可