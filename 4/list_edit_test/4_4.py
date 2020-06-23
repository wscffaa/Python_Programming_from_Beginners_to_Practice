# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 11:03
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 4_4.py
# @Software: PyCharm
'''
一百万：创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这
些数字打印出来（如果输出的时间太长，按Ctrl + C 停止输出，或关闭输出窗口）。
'''

numbers = [value for value in range(1,1000001)]
print(numbers)