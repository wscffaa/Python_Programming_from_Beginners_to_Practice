# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 11:12
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : slice_list.py
# @Software: PyCharm

#要创建切片，可指定要使用的第一个元素和最后一个元素的索引。
#与函数range()一样，Python在到达你指定的第二个索引前面的元素后停止。
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#如果你没有指定第一个索引，Python将自动从列表开头开始
print(players[:2])
#要让切片终止于列表末尾，也可使用类似的语法。
print(players[0:])
#负数索引返回离列表末尾相应距离的元素
print(players[-2:])

#4.4.2 for循环遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team: ")
for player in players[0:3]:
    print(player.title())

#4.4.3 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  #不指定任何索引的情况下就是从第一个到最后一个
my_foods.append('cannoli')
friend_foods.append('ice cream')  #复制列表只是把第一个列表中的元素复制到另外一个全新的列表，将my_foods的副本存储到friend_foods，之后再无关联
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are: ")
print(friend_foods)