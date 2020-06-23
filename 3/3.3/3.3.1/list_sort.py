# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 20:31
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : list_sort.py
# @Software: PyCharm

#sort()永久性排序，无法恢复到原来的排序状态
#sort()函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。默认是正向排序。
#reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
The_guest = ['Mao YuWei','Gongzhe','Guo Chongye','Lin jincan']
The_guest.sort()
print(The_guest)  #是按字母顺序排列
The_guest.sort(reverse=True)
print(The_guest)  #字母顺序相反的顺序排列,对列表元素排列顺序的修改是永久性的