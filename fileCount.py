# -*- coding: utf-8 -*-
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
import os
l=[]
for root, dirs, files in os.walk('D:\\aliDoc'):
    #print(root, "consumes", end=" ")
    if len(files)>0:
        l=l+list([(name,os.path.getsize(os.path.join(root, name))) for name in files])
    #print("bytes in", len(files), "non-directory files")
print('总共有',len(l),'个文件')
l.sort()    
l.reverse()
for i in l:
    print(i)    