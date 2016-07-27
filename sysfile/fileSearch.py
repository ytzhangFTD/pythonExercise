# -*- coding: utf-8 -*-
# print('hello,world!')
# 当前文件目录下所有目录及所有文件
# 统计 文件类型 大小 
# 
import os
#列出当前目录下的所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]
#列出当前目录下的所有文件
[x for x in os.listdir('.') if os.path.isfile(x)]
#列出当前目录下所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']





