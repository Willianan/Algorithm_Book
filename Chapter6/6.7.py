# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/17 12:31
Project:AlgorithmBook
Filename:6.7.py
"""

"""
如何按要求比较两个数的大小
题目描述：如何比较a、b两个数的大小？不能使用大于、小于以及if语句。
"""
# 绝对值法
def maxs(a,b):
	return (a+b+abs(a-b))//2

if __name__ == "__main__":
	print(maxs(8,6))