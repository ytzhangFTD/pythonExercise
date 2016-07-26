# -*- coding: utf-8 -*-
# print('hello,world!')
# 处理文本文件 word count
# 统计 多少个汉字，多少个英文,多少个符号
# [20,64] [91,96][123,126]字符 [65,90] [97,122]英文字母
def ishan(text):
    # for python 3.x
    # sample: ishan('一') == True, ishan('我&&你') == False
	#for char in text:
	#	print(u'\u4e00' <=char<= u'\u9fff')
	#	print(str(char))
    return all(u'\u4e00' <= char <= u'\u9fff' for char in text)
#print(ishan('一天'))
wordCount=0
charCount=0
f=open('test.txt','r',encoding='utf-8')#指定读取文件编码
while 1:
    lines = f.readlines(1024)#缓存读取文件
    if not lines:
        break
    for line in lines:#
        #print(str(line))
        for char in str(line):#对文件一行中每个字符做判断
            if ishan(char):#中文判断
                wordCount=wordCount+1
            elif ((65<=ord(char)<=90) or (97<=ord(char)<=122)):
                charCount=charCount+1
print('中文有',wordCount,'个')
print('英文字符有',charCount,'个')


