# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 21:24
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : Delete_list_elements.py
# @Software: PyCharm

#从列表中删除元素
  #1.使用del语句删除元素,使用del可删除任何位置处的列表元素，条件是知道其索引。
  #使用del语句将值从列表中删除后，你就无法再访问它了。

transportation = ['Car','Motocycles','Subway']
del transportation[1]
print(transportation)


  #2.使用pop()方法删除元素
  #有时候，你要将元素从列表中删除，并接着使用它的值。
  #方法pop()可删除列表末尾的元素，并让你能够接着使用它。
  #术语弹出（pop）源自这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。

transportation1 = ['Car','Motocycles','Subway']
transportation1.pop()
print(transportation1)
print(transportation1.pop()) #删除后依旧能访问被删除的值


  #3.弹出列表中任何位置处的元素
  #使用pop()来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。
motorcycles = ['Honda','Yamaha','Suzuki']
first_owned = motorcycles.pop(1)
print('The first motorcycle I owned was a ' + first_owned + '.')
               #每当你使用pop()时，被弹出的元素就不再在列表中了。

'''
如果你不确定该使用del语句还是pop()方法，下面是一个简单的判断标准：如果你要从列表
中删除一个元素，且不再以任何方式使用它，就使用del语句；如果你要在删除元素后还能继续
使用它，就使用方法pop()。
'''

  #4.根据值删除元素
  #知道值，不知道位置，可使用方法remove()。
  #使用remove()从列表中删除元素时，也可接着使用它的值。
transportation2 = ['Car','Motocycles','Subway']
too_expensive = 'Car'
transportation2.remove(too_expensive)
print(transportation2)
print('\nA ' + too_expensive.title() + " is too expensive for me. ")  #remove后的值任然可以被使用，只是从列表中删除，代号为列表.remove()

