# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 21:28
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 3_8.py
# @Software: PyCharm
'''
想出至少5 个你渴望去旅游的地方。
 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始
Python 列表。
 使用sorted()按字母顺序打印这个列表，同时不要修改它。
 再次打印该列表，核实排列顺序未变。
 使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它。
 再次打印该列表，核实排列顺序未变。
 使用reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
 使用reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来
的排列顺序。
 使用sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺
序确实变了。
 使用sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，
核实排列顺序确实变了。
'''
City = ['Shanghai','Changsha','Chongqing','Hangzhou','Suzhou']
print(City)

print(sorted(City))
print(City)

print(sorted(City,reverse=True))
print(City)

City.reverse()
print(City)

City.reverse()
print(City)

City.sort()
print(City)

City.sort(reverse=True)
print(City)