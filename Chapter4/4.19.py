# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 21:13
Project:AlgorithmBook
Filename:4.19.py
"""

"""
如何按要求构造新的数组
题目描述：给定一个数组a[N],希望构造一个新的数组b[N]，其中，b[i]=a[0]*a[1]*a[2]*·····*a[N-1]/a[i]。
在构造数组的过程中，由如下几点要求：
(a)、不允许使用除法；
(b)、要求O(1)空间复杂度和O[N]时间复杂度；
(c)、除遍历计算器与a[N]、b[N]外，不可以使用新的变量(包括栈临时变量、堆空间和全局静态变量等)；
(d)、请用程序实现并简单描述。
"""

def calculate(a,b):
	b[0] = 1
	N = len(a)
	i = 1
	while i < N:
		b[i] = b[i-1]*a[i-1]                    # 正向计算乘积
		i += 1
	b[0] = a[N-1]
	i = N-2
	while i >= 1:
		b[i] *= b[0]
		b[0] *= a[i]                            # 逆向计算乘积
		i -= 1

if __name__ == "__main__":
	a = [1,2,3,4,5,6,7,8,9,10]
	b = [None]*len(a)
	calculate(a,b)
	i = 0
	while i < len(b):
		print(b[i],end=' ')
		i += 1