# -*- coding: gbk -*-
# print('hello,world!')
# �����ı��ļ� word count
# ͳ�� ���ٸ����֣����ٸ�Ӣ��,���ٸ�����
# [20,64] [91,96][123,126]�ַ� [65,90] [97,122]Ӣ����ĸ
def ishan(text):
    return all('\u4e00' <= char <= '\u9fff' for char in text)


print(ishan('һ��'))
# with open('test.txt','r') as f
# wordCount=0
# charCount=0
# for


