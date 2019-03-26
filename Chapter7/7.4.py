# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/19 11:05
Project:AlgorithmBook
Filename:7.4.py
"""

"""
如何用一个随机函数得到另外一个随机函数
题目描述：有一个函数func1能返回0和1两个值，返回0和1的概率都是1/2，问怎么利用这个函数得到另一个
函数func2，使得func2也只能返回0和1，且返回0的概率为1/4，返回1的概率为3/4。
"""
import random
# 返回0和1的概率都为1/2
def func1():
	return int(round(random.random()))

# 返回0的概率为1/4.返回1的概率为3/4
def func2():
	a1 = func1()
	a2 = func1()
	tmp = a1
	tmp |= (a2 << 1)
	if tmp == 0:
		return 0
	else:
		return 1


if __name__ == "__main__":
	i = 0
	while i < 16:
		print(func2(),end='')
		i += 1
	print()
	i = 0
	while i < 16:
		print(func2(),end='')
		i += 1