# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/28 16:22
Project:AlgorithmBook
Filename:4.7.py
"""

"""
如何求数组中两个元素的最小距离
题目描述：给定一个整数数组，数组中含有重复元素，给定两个数字num1和num2，求这两个数字在数组中出现
的位置的最小距离。
"""

# 方法一：蛮力法
def minDistance1(array,num1,num2):
	if array == None or len(array) < 1:
		print("参数不合理")
		return 2**32
	minDis = 2**32              # num1和num2的最小距离
	dist = 0
	i = 0
	while i < len(array):
		if array[i] == num1:
			j = 0
			while j < len(array):
				if array[j] == num2:
					dist = abs(i - j)               # 当前遍历的num1和num2的距离
					if dist < minDis:
						minDis = dist
				j += 1
		i += 1
	return minDis

# 方法二：动态规划
def minDistance2(array,num1,num2):
	if array == None or len(array) < 1:
		print("参数不合理")
		return 2**32
	lastPos1 = -1                           # 上次遍历到num1的位置
	lastPos2 = -1                           # 上次遍历到num2的位置
	minDis = 2**32                          # num1和num2的最小距离
	i = 0
	while i < len(array):
		if array[i] == num1:
			lastPos1 = i
			if lastPos2 >= 0:
				minDis = min(minDis,lastPos1 - lastPos2)
		if array[i] == num2:
			lastPos2 = i
			if lastPos1 >= 0:
				minDis = min(minDis,lastPos2-lastPos1)
		i += 1
	return minDis


if __name__ == "__main__":
	array = [4,6,7,4,7,4,6,4,7,8,5,6,4,3,10,8]
	num1 = 4
	num2 = 8
	print(minDistance1(array,num1,num2))
	print(minDistance2(array,num1,num2))