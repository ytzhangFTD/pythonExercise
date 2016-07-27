# -*- coding: utf-8 -*-
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def normalize(name):
    name=name.lower()
    name=name[0].upper()+name[1:]
    return name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce
def f(x,y):
    return x*y
def prod(L):
    return reduce(f,L)
#print('3 * 5 * 7 * 9 =', reduce(f,[3, 5, 7, 9]))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))



        