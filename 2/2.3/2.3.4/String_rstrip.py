# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 15:54
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : String_rstrip.py
# @Software: PyCharm
#string.strip(s[, chars])，它返回的是字符串的副本，并删除前导和后缀字符。（意思就是你想去掉字符串里面的哪些字符，那么你就把这些字符当参数传入。此函数只会删除头和尾的字符，中间的不会删除。）如果strip()的参数为空，那么会默认删除字符串头和尾的空白字符(包括\n，\r，\t这些)。

#剔除字符串开头的空白，或同时剔除字符串两端的空白。为此，可分别使用方法lstrip()和strip()：
name = " \rPy thon\n\t "
name1 = name.rstrip()   #rstrip()去掉结尾
print(name1)
print(len(name1))

name2 = name.strip()   #strip（）去掉开头和结尾
print(name2)
print(len(name2))

name3 = name.lstrip()  #lstrip()去掉开头
print(name3)
print(len(name3))

a="babacb111baccbb"
print(a.lstrip("abc"))  #带参数去掉开头，abc三个参数分开来查找并删除
print(a.rstrip("abc"))  #带参数去掉结尾的参数