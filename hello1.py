# -*- coding: utf-8 -*-
# print('hello,world!')
# �����ı��ļ� word count
# ͳ�� ���ٸ����֣����ٸ�Ӣ��,���ٸ�����
# [20,64] [91,96][123,126]�ַ� [65,90] [97,122]Ӣ����ĸ
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(10)	
# with open('test.txt','r') as f
# wordCount=0
# charCount=0
# for


