# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 20:56
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 3_7.py
# @Software: PyCharm
'''
缩减名单：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
 以完成练习3-6 时编写的程序为基础，在程序末尾添加一行代码，打印一条你只
能邀请两位嘉宾共进晚餐的消息。
 使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹
出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进
晚餐。
 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
 使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程
序结束时名单确实是空的。
'''
The_guest = ['Mao YuWei','Gongzhe','Guo Chongye','Lin jincan']
print("I find a bigger dinner table. ")
The_guest.insert(0,'Xiao Bei')
The_guest.insert(3,'Han Han')
The_guest.append('Gou Pi')
print(The_guest)
for index in The_guest:
    print(index + ", Would you like to have dinner with me ?")  #index即代表列表元素

print(str(The_guest) + ", I can only invite two guests")

n = int(len(The_guest))  #n设置为数组长度
while n > 2 :
    last_person = The_guest.pop()
    print(last_person + "i am so sorry , I can't have dinner with you. ")
    n = n - 1

for index in The_guest:
    print(index + "you can still have dinner with me . ")

del The_guest[0:2]
print(The_guest)


