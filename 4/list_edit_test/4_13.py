# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 14:04
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 4_13.py
# @Software: PyCharm

'''
4-13 自助餐：有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食
品，并将其存储在一个元组中。
 使用一个for 循环将该餐馆提供的五种食品都打印出来。
 尝试修改其中的一个元素，核实Python 确实会拒绝你这样做。
 餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：
给元组变量赋值，并使用一个for 循环将新元组的每个元素都打印出来
'''
print("The initial menu is as follows:")
foods = ("apple","lemon","pear","strawberry","cherry")
for food in foods:
    print(food)
# food[0] ="fruits" #TypeError: 'str' object does not support item assignment
foods = ("biscuits","noodles","pear","strawberry","cherry")
print("\nThe new menu is as follows:")
for food in foods:
    print(food)