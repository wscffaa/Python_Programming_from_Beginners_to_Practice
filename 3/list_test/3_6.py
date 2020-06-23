# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 22:33
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 3_6.py
# @Software: PyCharm

'''
添加嘉宾：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀
请哪三位嘉宾。
 以完成练习3-4 或练习3-5 时编写的程序为基础，在程序末尾添加一条print 语
句，指出你找到了一个更大的餐桌。
 使用insert()将一位新嘉宾添加到名单开头。
 使用insert()将另一位新嘉宾添加到名单中间。
 使用append()将最后一位新嘉宾添加到名单末尾。
 打印一系列消息，向名单中的每位嘉宾发出邀请。
'''
The_guest = ['Mao YuWei','Gongzhe','Guo Chongye','Lin jincan']
print("I find a bigger dinner table. ")
The_guest.insert(0,'Xiao Bei')
The_guest.insert(3,'Han Han')
The_guest.append('Gou Pi')
print(The_guest)
for index in The_guest:
    print(index + ", Would you like to have dinner with me ?")  #index即代表列表元素