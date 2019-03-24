# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/17 12:41
Project:AlgorithmBook
Filename:6.8.py
"""

"""
如何求有序数列的第1500个数的值
题目描述：有一个有序数列，序列中的每一个值都能够被2或3或5所整除，1是这个序列的第一个元素。求第1500个值是多少？
"""
#方法一：蛮力法
def searth(n):
	i = 0
	count = 0
	i = 1
	while True:
		if i % 2== 0 or i % 3 == 0 or i % 5 == 0:
			count += 1
		if count == n:
			break
		i += 1
	return i


# 方法二：数组规律法
def searth2(n):
	a = [0,2,3,4,5,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,30]
	ret = (n//22)*30+a[n%22]
	return ret
if __name__ == "__main__":
	print(searth(1500))
	print(searth2(1500))