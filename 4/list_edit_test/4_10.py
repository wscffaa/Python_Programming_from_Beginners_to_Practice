# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 13:39
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 4_10.py
# @Software: PyCharm

'''
切片：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个
元素。
 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中
间的三个元素。
 打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三
个元素。
'''

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:3])  #前三个
print(players[1:4])  #之间三个
print(players[-3:])  #后三个