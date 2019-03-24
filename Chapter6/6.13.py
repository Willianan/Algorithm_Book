# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/17 14:21
Project:AlgorithmBook
Filename:6.13.py
"""

"""
如何在不能使用库函数的条件下计算n的平方根
题目描述：给定一个数n，求出它的平方根。
"""
def squareRoot(n,e):
	new_one = n
	last_one = 1.0
	while new_one - last_one > e:                                   # 直到满足精度要求为止
		new_one = (new_one+last_one)/2                              # 求下一个近似值
		last_one = n / new_one
	return new_one



if __name__ == "__main__":
	n = 50
	e = 0.000001
	print(str(n)+"的平方根为："+str(squareRoot(n,e)))
	n = 4
	print(str(n)+"的平方根为："+str(squareRoot(n,e)))