# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 10:54
Project:AlgorithmBook
Filename:4.10.py
"""

"""
如何求数组连续最大和
题目描述：一个有n个元素的数组，这n个元素既可以是正数也可以是负数，数组中连续的一个或几个元素可以组成一个连续的子数组，
一个数组可能有多个这种连续的子数组，求子数组和的最大值。
"""

# 方法一：蛮力法
def maxSubArray1(array):
	if array == None or len(array) < 1:
		print("数组不存在")
		return
	ThisSum =  0
	MaxSum = 0
	i = 0
	while i < len(array):
		j = i
		while j < len(array):
			ThisSum = 0
			k = i
			while k < j:
				ThisSum += array[k]
				k += 1
			if ThisSum > MaxSum:
				MaxSum = ThisSum
			j += 1
		i += 1
	return MaxSum

# 方法二：重复利用已经计算的子数组和
def maxSubArray2(array):
	if array == None or len(array) < 1:
		print("数组不存在")
		return
	maxSum = -2**31
	i = 0
	while i < len(array):
		sums = 0
		j = i
		while j < len(array):
			sums += array[j]
			if sums > maxSum:
				maxSum = sums
			j += 1
		i += 1
	return maxSum

# 动态规划方法
def maxSubArray3(array):
	if array == None or len(array) < 1:
		print("数组不存在")
		return
	End = [None]*len(array)
	All = [None]*len(array)
	End[len(array)-1] = array[len(array)-1]
	All[len(array)-1] = array[len(array)-1]
	End[0] = All[0] = array[0]
	i = 1
	while i < len(array):
		End[i] = max(End[i-1]+array[i],array[i])
		All[i] = max(End[i],All[i-1])
		i += 1
	return All[len(array)-1]

# 方法四：优化的动态规划方法
def maxSubArray4(array):
	if array == None or len(array) < 1:
		print("数组不存在")
		return
	nAll = array[0]                             # 最大子数组和
	nEnd = array[0]                             # 包含最后一个元素的最大子数组和
	i= 1
	while i < len(array):
		nEnd = max(nEnd+array[i],array[i])
		nAll = max(nEnd,nAll)
		i += 1
	return nAll



if __name__ == "__main__":
	array = [1,-2,4,8,-4,7,-1,-5]
	print("连续最大和为：",maxSubArray1(array))
	print("连续最大和为：",maxSubArray2(array))
	print("连续最大和为：",maxSubArray3(array))
	print("连续最大和为：",maxSubArray4(array))


"""
引申：在知道子数组最大值后，如何才能确定最大子数组的位置
"""
class Test:
	def __init__(self):
		self.begin = 0                      # 记录最大子数组起始位置
		self.end = 0                        # 记录最大子数组结束位置

	def maxSubArray(self,array):
		maxSum = -2**31                     # 子数组最大值
		nSum = 0                            # 包含子数组最后一位的最大值
		nStart = 0
		i = 0
		while i < len(array):
			if nSum < 0:
				nSum = array[i]
				nStart = i
			else:
				nSum += array[i]
			if nSum > maxSum:
				maxSum = nSum
				self.begin = nStart
				self.end = i
			i += 1
		return maxSum
	def getBegin(self):
		return self.begin
	def getEnd(self):
		return self.end