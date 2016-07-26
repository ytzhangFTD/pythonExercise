# -*- coding: utf-8 -*-
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def person(name, gender, **wk):
    print('{name:%s;gender:%s;other:%s}' %(name,gender,wk))
    
#person('ytzhang',12,city='beijing',time='20160725')



def test(a,b,c=0,*args,city='beijing',**wk):
    print('a=',a,'b=',b,'c=',c,'args=',args,'wk=',wk,'city=',city)
    
#test('a','b',4,'c','d',time='20160725',city='beijing')
test('a','b',city='Hangzhou')

