# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/17 14:21
Project:AlgorithmBook
Filename:6.15.py
"""

"""
如何不使用循环输出1到100
题目描述：实现一个函数，要求在不使用循环的前提下输出1到100
"""
def prints(n):
	if n > 0:
		prints(n-1)
		print(str(n),end=' ')

if __name__ == "__main__":
	prints(100)