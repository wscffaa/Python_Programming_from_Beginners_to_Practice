# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 10:52
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : Create_values_list.py
# @Software: PyCharm

#列表非常适合用于存储数字集合，而Python提供了很多工具，可帮助你高效地处理数字列表

#4.3.1 range(start, stop, step)  step是步长
#输出不包含stop,使用range()时，如果输出不符合预期，请尝试将指定的值加1或减1。
for value in range(0,5):
    print(value)

#4.3.2 要创建数字列表，可使用函数list()将range()的结果直接转换为列表。如果将range()作为list()的参数，输出将为一个数字列表.
numbers = list(range(1,18,2))
print(numbers)

squares = []
for value in range(1,11):
    value = value**2    #使用临时变量，让代码更容易理解
    squares.append(value)
    print(squares)


#4.3.3 对数字列表执行简单的统计计算
print(sum(squares))
print(min(squares))
print(max(squares))

#4.3.4 列表解析!!最好使用，很方便
test = [value**2 for value in range(1,11)]   #[表达式 for循环赋值]
print(test)

