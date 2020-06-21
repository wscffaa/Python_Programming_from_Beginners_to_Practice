# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 10:24
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : list.py
# @Software: PyCharm

'''
列表由一系列按特定顺序排列的元素组成。
在Python中，用方括号[]来表示列表，并用逗号来分隔其中的元素。
'''

#访问列表元素，要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内
bicycles = ['trek','cannodale','redline','specialized']
print(bicycles[1].title())
#当你请求获取列表元素时，Python只返回该元素，而不包括方括号和引号
#使用title()来规范输出