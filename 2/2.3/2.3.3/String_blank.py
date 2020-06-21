# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 15:49
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : String_blank.py
# @Software: PyCharm
#使用制表符或换行符来添加空白
#在编程中，空白泛指任何非打印字符，如空格、制表符和换行符.
#\r 表示将光标的位置回退到本行的开头位置
#\b 表示将光标的位置回退一位
Name = "Taylor Swift"
print("Name\tName")  #在字符串中添加制表符，可使用字符组合\t
print("Nme\nName")   #在字符串中添加换行符，可使用字符组合\n
print("Name\n\tName")#在同一个字符串中同时包含制表符和换行符。