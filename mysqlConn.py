# -*- coding: utf-8 -*-
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
import pymysql
conn = pymysql.connect(host='localhost', port=3306,user='root',passwd='123456',db='test',charset='UTF8')
cur = conn.cursor()
cur.execute("select version()")
for i in cur:
    print(i)
cur.close()
conn.close()    