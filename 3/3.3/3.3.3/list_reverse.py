# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 20:53
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : list_reverse.py
# @Software: PyCharm

#reverse()不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序：
The_guest = ['Mao YuWei','Gongzhe','Guo Chongye','Lin jincan']
The_guest.reverse()
print(The_guest) #方法reverse()永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此只需对列表再次调用reverse()即可。
The_guest.reverse()
print(The_guest)