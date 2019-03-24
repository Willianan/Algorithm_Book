# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/17 14:21
Project:AlgorithmBook
Filename:6.12.py
"""

"""
如何计算一个数的n次方
题目描述：给定一个数d和n，如何计算d的n次方？
"""

'''
****** 方法功能：计算一个数的n次方
****** 输入参数：d为底数，你为幂
****** 返回值：  d^n
'''
def power(d,n):
	if n == 0:
		return 1
	if n == 1:
		return d
	result = 1.0
	if n > 0:
		i = 1
		while i <= n:
			result *= d
			i += 1
		return result
	else:
		i = 1
		while i <= abs(n):
			result /= d
			i += 1
		return result


if __name__ == "__main__":
	print(power(2,3))
	print(power(-2,3))
	print(power(2,-3))