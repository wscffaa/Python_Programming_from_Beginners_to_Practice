# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 11:03
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 4_5.py
# @Software: PyCharm
'''
计算1~1 000 000 的总和：创建一个列表，其中包含数字1~1 000 000，再使用
min()和max()核实该列表确实是从1 开始，到1 000 000 结束的。另外，对这个列表调
用函数sum()，看看Python 将一百万个数字相加需要多长时间。
'''
numbers = [value for value in range(1,1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))