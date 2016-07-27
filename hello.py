# -*- coding: utf-8 -*-
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
import pymysql,os
def getConn():
    conn = pymysql.connect(host='localhost', port=3306,user='root',passwd='123456',db='test',charset='UTF8')
    return conn
def closeConn(conn):
    if conn:
        conn.close()
# 查询文件 【文件名，文件大小】
def fileCount(filePath):
    l=[]
    for root, dirs, files in os.walk(filePath):
        if len(files)>0:
            l=l+list([(name,os.path.getsize(os.path.join(root, name))) for name in files])
    return l
def addfile():
    l=fileCount('D:\\aliDoc')
    conn=getConn()
    try:
        cur = conn.cursor()
        for i in l:
            cur.execute('insert into file(name,size) values(%s,%s)', i)
        conn.commit()
        cur.close()
    finally:
        if conn:
            conn.close()
addfile()
        