# -*- coding: utf-8 -*-
# print('hello,world!')
# 处理文本文件 word count
# 统计 多少个汉字，多少个英文,多少个符号
# [20,64] [91,96][123,126]字符 [65,90] [97,122]英文字母
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


