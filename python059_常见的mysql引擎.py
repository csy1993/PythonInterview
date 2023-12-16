'''
@Author: CSY
@Date: 2020-02-07 17:04:51
@LastEditors  : CSY
@LastEditTime : 2020-02-07 17:12:46
'''
"""
59、列出常见MYSQL数据存储引擎
"""
# InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。如果需要对事务的完整性要求比较高（比如银行），
# 要求实现并发控制（比如售票），那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，因为支持事务的提交（commit）和回滚（rollback）。 

# MyISAM：插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读出记录，那么选择MyISAM能实现处理高效率。如果应用的完整性、并发性要求比 较低，也可以使用。

# MEMORY：所有的数据都在内存中，数据的处理速度快，但是安全性不高。如果需要很快的读写速度，对数据的安全性要求较低，可以选择MEMOEY。
# 它对表的大小有要求，不能建立太大的表。所以，这类数据库只使用在相对较小的数据库表。

