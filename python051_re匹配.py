'''
@Author: CSY
@Date: 2020-02-06 17:49:12
@LastEditors  : CSY
@LastEditTime : 2020-02-06 18:02:40
'''
"""
51、正则匹配，匹配日期2018-03-20
"""
import re
url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-21&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
res=re.findall(r'\d{4}-\d{1,2}-\d{1,2}',url)
print(res)