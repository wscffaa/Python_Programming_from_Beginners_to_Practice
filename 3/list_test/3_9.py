# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 21:28
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 3_9.py
# @Software: PyCharm

'''
晚餐嘉宾：在完成练习3-4~练习3-7 时编写的程序之一中，使用len()打印一
条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
'''

The_guest = ['Mao YuWei','Gongzhe','Guo Chongye','Lin jincan']
for index in The_guest:
    print(index + ", Would you like to have dinner with me ?")  #index即代表列表元素
print('There are ' + str(len(The_guest)) + ' guests have dinner with me . ')