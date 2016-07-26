# -*- coding: gbk -*-
# print('hello,world!')
# 处理文本文件 word count
# 统计 多少个汉字，多少个英文,多少个符号
# [20,64] [91,96][123,126]字符 [65,90] [97,122]英文字母
def ishan(text):
    return all('\u4e00' <= char <= '\u9fff' for char in text)


print(ishan('一天'))
# with open('test.txt','r') as f
# wordCount=0
# charCount=0
# for


