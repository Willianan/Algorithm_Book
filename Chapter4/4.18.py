# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 20:34
Project:AlgorithmBook
Filename:4.18.py
"""

"""
如何判断请求能否在给定的存储条件下完成
题目描述：给定一台有m存储空间的机器，有n个请求需要在这台机器上运行，第i个请求计算时需要占
R[i]空间，计算结果需要占O[i]个空间(O[i]<R[i]).请设计一个算法，判断中n个请求能否全部完成。
若能，给出这n个请求的安排顺序。
"""
def swap(array,i,j):
	tmp = array[i]
	array[i] = array[j]
	array[j] = tmp

# 按照R[i]-O[i]由大到小进行排序
def bubbleSort(R,O):
	i = 0
	while i < len(R) - 1:
		j = len(R) - 1
		while j > i:
			if R[j]-O[j] > R[j-1]-O[j-1]:
				swap(R,j,j-1)
				swap(O,j,j-1)
			j -= 1
		i += 1
def schedule(R,O,M):
	bubbleSort(R,O)
	left = M                            # 剩余可用的空间数
	i = 0
	while i < len(R):
		if left < R[i]:                 # 剩余的空间数无法继续处理第i个请求
			return False
		else:                           # 剩余的空间数能继续处理第i个请求，处理完成后将占用O[i]个空间
			left -=O[i]
		i += 1
	return True

if __name__ == "__main__":
	R = [10,15,23,20,6,9,7,16]
	O = [2,7,8,4,5,8,6,8]
	N = 8
	M = 50
	scheduleResult = schedule(R,O,M)
	if scheduleResult:
		print("按照如下请求序列可以完成：")
		i= 0
		while i < N:
			print(str(R[i])+","+str(O[i]),end=' ')
			i += 1
	else:
		print("无法完成调度")