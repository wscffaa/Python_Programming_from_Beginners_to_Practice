# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 22:10
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 3——5.py
# @Software: PyCharm

'''
修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
 以完成练习3-4 时编写的程序为基础，在程序末尾添加一条print 语句，指出哪
位嘉宾无法赴约。
 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
'''

The_guest = ['Mao YuWei','Gongzhe','Guo Chongye','Lin jincan']
for index in The_guest:
    print(index + ", Would you like to have dinner with me ?")  #index即代表列表元素

print(The_guest[3] + " can't go to the dinner.")
The_guest[3] = "Xiao Bei"
for index in The_guest:
    print(index + ", Would you like to have dinner with me ?")