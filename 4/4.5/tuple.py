# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 13:51
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : tuple.py
# @Software: PyCharm

'''
列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网
站的用户列表或游戏中的角色列表至关重要。然而，有时候你需要创建一系列不可修改的元素，
元组可以满足这种需求。Python将不能修改的值称为不可变的，而不可变的列表被称为元组。

元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来
访问其元素，就像访问列表元素一样。

元组不可变，但储存元组的变量却可以变
'''
dimensions = (200,50)
for dimension in dimensions:   #元组中的元素一样可以用for循环遍历
    print(dimension)

#虽然不能修改元组的元素，但可以给存储元组的变量赋值。
dimensions = (400,200)   #，将一个新元组存储到变量dimensions中
print("\nModified dimensions:")
for dimension in dimensions :
    print(dimension)
#。如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组。