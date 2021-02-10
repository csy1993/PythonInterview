'''
@Author: CSY
@Date: 2020-02-07 16:36:41
@LastEditors  : CSY
@LastEditTime : 2020-02-07 16:40:45
'''
"""
55、求三个方法打印结果
fn("one",1）直接将键值对传给字典；
fn("two",2)因为字典在内存中是可变数据类型，所以指向同一个地址，传了新的额参数后，会相当于给字典增加键值对
fn("three",3,{})因为传了一个新字典，所以不再是原先默认参数的字典
"""
def get_dict(key,value,dict01={}):
    dict01[key]=value
    print(dict01)

get_dict('one',1)
get_dict('two',2)
get_dict("three",3,{})