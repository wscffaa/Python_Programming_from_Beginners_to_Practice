# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 10:41
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 3_2.py
# @Software: PyCharm
'''
问候语：继续使用练习3-1 中的列表，但不打印每个朋友的姓名，而为每人打
印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
'''
names = ['Cai_feifan','Mao_yuwei','Lin_jincan','Guo_chongye','Gong_zhe']
for index in names :
    print(index,", Are you OK ？")

'''
提前插入for循环，简单便捷，具体格式如下：
        for 迭代变量 in 字符串|列表|元组|字典|集合：
            代码块
'''