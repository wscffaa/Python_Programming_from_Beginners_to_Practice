# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 11:04
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 4_8.py
# @Software: PyCharm
'''
立方：将同一个数字乘三次称为立方。例如，在Python 中，2 的立方用2**3
表示。请创建一个列表，其中包含前10 个整数（即1~10）的立方，再使用一个for 循
环将这些立方数都打印出来。
'''
squares = [value**2 for value in range(1,11)]
print(squares)