# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 11:04
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 4_6.py
# @Software: PyCharm
'''
奇数：通过给函数range()指定第三个参数来创建一个列表，其中包含1~20 的
奇数；再使用一个for 循环将这些数字都打印出来。
'''
odd_numbers = [value for value in range(1,21,2)]
print(odd_numbers)