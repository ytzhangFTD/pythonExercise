# -*- coding: utf-8 -*-
import pymysql,os
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello,Flask!'
@app.route('/hello')
def hello():
    return 'Hello,Hello!'
@app.route('/test')
def test():
    addfile()
    return 'OK!'

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
        cur.close()
        conn.close()
    finally:
        conn.close()
        