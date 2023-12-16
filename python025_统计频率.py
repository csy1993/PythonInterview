'''
@Author: CSY
@Date: 2020-01-27 18:07:45
@LastEditors  : CSY
@LastEditTime : 2020-01-27 20:33:40
'''
"""
25、利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
"""
from collections import Counter
str01="kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
print(Counter(str01))