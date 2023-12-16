'''
@Author: CSY
@Date: 2020-01-13 22:06:44
@LastEditors  : CSY
@LastEditTime : 2020-01-13 22:16:30
'''
"""
16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
"""
import re

str01="<div class='nam'>中国</div>"
res=re.findall(r"<div class='.*'>(.*?)</div>",str01)
print(res)