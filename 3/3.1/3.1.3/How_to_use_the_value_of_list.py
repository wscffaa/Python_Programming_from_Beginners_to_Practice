# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 10:31
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : How_to_use_the_value_of_list.py
# @Software: PyCharm

#可像使用其他变量一样使用列表中的各个值。
#你可以使用拼接根据列表中的值来创建消息.
Name = ['Cai fei fan', 'Mao Yu Wei']
Message = "My name is " + Name[0] + " and My girlfriend is " + Name[-1] + "!"
print(Message)