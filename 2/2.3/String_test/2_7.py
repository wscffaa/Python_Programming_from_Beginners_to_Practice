# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 10:36
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 2_7.py
# @Software: PyCharm

#剔除人名中的空白：存储一个人名，并在其开头和末尾都包含一些空白字符。
#务必至少使用字符组合"\t"和"\n"各一次。
#打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip()、
#rstrip()和strip()对人名进行处理，并将结果打印出来。
Name = " \tTaylor Swift\t "

print(Name)
print(len(Name))   #Name的原本长度

print(len(Name.strip()))  #去掉两端空白后的长度
print(Name.strip())

print(len(Name.rstrip()))  #去掉后端空白后的长度
print(Name.rstrip())

print(len(Name.lstrip()))  #去掉前端空白后的长度
print(Name.lstrip())