# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/28 14:47
Project:AlgorithmBook
Filename:4.4.py
"""

"""
如何找出数组中丢失的数
题目描述：给定一个由n-1个整数组成的未排序的数组序列，其元素都是1到n中的不同的整数。
请写出一个寻找数组序列中缺失整数的线性时间算法。
"""
#方法一：累加求和
def getNum1(array):
	if array == None or len(array) <= 0:
		print("参数不合理")
		return -1
	suma = 0
	sumb = 0
	i = 0
	while i < len(array):
		suma = suma + array[i]
		sumb = sumb + i
		i += 1
	sumb = sumb + len(array) + len(array) + 1
	return sumb - suma

# 方法二：异或法
def getNum2(array):
	if array == None or len(array) <= 0:
		print("参数不合理")
		return -1
	a = array[0]
	b = 1
	i = 1
	while i < len(array):
		a = a ^ array[i]
		i += 1
	i = 2
	while i <= len(array)+1:
		b = b ^ i
		i += 1
	return a ^ b

if __name__ == "__main__":
	array = [1,4,3,2,7,5]
	print(getNum1(array))
	print(getNum2(array))