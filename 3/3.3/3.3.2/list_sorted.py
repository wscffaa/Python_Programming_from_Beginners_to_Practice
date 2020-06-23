# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 20:35
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : list_sorted.py
# @Software: PyCharm

#要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数sorted()。
# 函数sorted()让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。
'''
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

sorted 语法：

sorted(iterable[, cmp[, key[, reverse]]])
参数说明：

iterable -- 可迭代对象。
cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）
'''
The_guest = ['Mao YuWei','Gongzhe','Guo Chongye','Lin jincan']
print(sorted(The_guest))
print(The_guest)  #调用函数sorted()后，列表元素的排列顺序并没有变
print(sorted(The_guest,reverse=True)) #按与字母顺序相反的顺序显示列表，也可向函数sorted()传递参数reverse=True