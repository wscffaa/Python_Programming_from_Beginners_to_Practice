# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 21:29
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 3_10.py
# @Software: PyCharm
'''
尝试使用各个函数：想想可存储到列表中的东西，如山岳、河流、国家、城
市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列表，
然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。
'''

Country = ['China','France','America','Australia']
print(Country[0].title())  #访问指定元素，titile()规范输出
print(Country[-1].title())
print("The best country in my mind is " + Country[0] + ".")
Country.append('Japan')
Country.append('korea')
Country.append('Thailand')
print(Country)
Last_Country = Country.pop()
print(Last_Country)  #从列表中删除依旧可以访问，pop弹出的意思
del Country[-1]
print(Country)  #del删除后无法访问
Riben = 'Japan'
Country.remove(Riben)
print(Riben + 'is a nice Country for taking a trip .') #Remove 以及可以访问列表移出的值
Country.insert(0,'Russia')   #任何位置插入使用Insert()
print(Country)
Country[0] = 'China'
Country[1] = 'Russia'
print(Country)

print(sorted(Country))   #函数sorted()让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。
print(Country)

print(sorted(Country,reverse=True))  #sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
print(Country)

Country.reverse()  #reverse() 函数没有返回值，但是会对列表的元素进行反向排序。
print(Country)

Country.reverse()
print(Country)

Country.sort() #list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值
print(Country)

Country.sort(reverse=True)
print(Country)

