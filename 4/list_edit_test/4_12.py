# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 13:39
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 4_12.py
# @Software: PyCharm
'''
4-12 使用多个循环：在本节中，为节省篇幅，程序foods.py 的每个版本都没有使用
for 循环来打印列表。请选择一个版本的foods.py，在其中编写两个for 循环，将各个
食品列表都打印出来。
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  #不指定任何索引的情况下就是从第一个到最后一个
my_foods.append('cannoli')
friend_foods.append('ice cream')  #复制列表只是把第一个列表中的元素复制到另外一个全新的列表，将my_foods的副本存储到friend_foods，之后再无关联
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are: ")
for food in friend_foods:
    print(food)


