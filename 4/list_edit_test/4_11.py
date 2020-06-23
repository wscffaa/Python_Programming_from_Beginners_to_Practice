# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 13:39
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 4_11.py
# @Software: PyCharm
'''
你的比萨和我的比萨：在你为完成练习4-1 而编写的程序中，创建比萨列表的
副本，并将其存储到变量friend_pizzas 中，再完成如下任务。
 在原来的比萨列表中添加一种比萨。
 在列表friend_pizzas 中添加另一种比萨。
 核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一
个for 循环来打印第一个列表；打印消息“My friend’s favorite pizzas are:”，再使
用一个for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
'''
My_Pizzas = ['Seafood pizza','Cheese pizza','Beef pizza','Chicken pizza']
Friend_Pizzas = My_Pizzas[:]
print("My favorite pizzas are: ")
for pizza in My_Pizzas:
    print(pizza)
print("My friends's favorite pizzas are: ")
for pizza in Friend_Pizzas:
    print(pizza)

