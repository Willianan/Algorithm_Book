# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/28 9:33
Project:AlgorithmBook
Filename:4.2.py
"""

"""
如何查找数组中元素的最大值和最小值
题目描述：给定数组a1,a2,a3,a4,······an,要求找出数组中的最大值和最小值。假设数组中的值两两各不相同
"""
# 方法一：蛮力法
# 方法二：分治法
class MaxMin1:
	def __init__(self):
		self.max = None
		self.min = None
	def getMax(self):
		return self.max
	def getMin(self):
		return self.min
	def GetmaxAndmin(self,array):
		if array == None:
			print("数组为空")
			return
		length = len(array)
		# 两两分组，把较小的数放在左半部分，较大的数放在右半部分
		i = 0
		while i < length-1:
			if array[i] > array[i+1]:
				tmp = array[i]
				array[i] = array[i+1]
				array[i+1] = tmp
			i += 2
		# 在各个分组的左半部分找最小值
		self.min = array[0]
		i = 2
		while i < length:
			if array[i] < self.min:
				self.min = array[i]
			i += 2
		# 在各个分组的左半部分找最大值
		self.max = array[1]
		i = 3
		while i < length:
			if array[i] > self.max:
				self.max = array[i]
			i += 2
		# 如果数组元素个数为奇数个，最后一个元素倍分为一组，需要特殊处理
		if length % 2 == 1:
			if self.max < array[length-1]:
				self.max = array[length-1]
			if self.min > array[length-1]:
				self.min = array[length-1]

# 方法三：变形的分治法
class MaxMin2:
	def getMAxMin(self,array,start,end):
		if array == None:
			print("数组为空")
			return
		list = []
		mid = (start + end) // 2
		if start == end:                      # l与r之间只有一个元素
			list.append(array[start])
			list.append(array[start])
			return list
		if start + 1 == end:                  # l与r之间只有2个元素
			if array[start] >= array[end]:
				max = array[start]
				min = array[end]
			else:
				max = array[end]
				min = array[start]
			list.append(min)
			list.append(max)
			return list
		# 递归计算左半部分
		lList = self.getMAxMin(array,start,mid)
		# 递归计算右半部分
		rList = self.getMAxMin(array,mid+1,end)
		# 计算总的最大值
		max = lList[1] if (lList[1] > rList[1]) else rList[1]
		# 计算总的最小值
		min = lList[0] if (lList[0] < rList[0]) else rList[0]
		list.append(min)
		list.append(max)
		return list

if __name__ == "__main__":
	array = [7,3,19,40,4,7,1]
	m = MaxMin1()
	m.GetmaxAndmin(array)
	print("max = ",m.getMax())
	print("min = ",m.getMin())
	m = MaxMin2()
	result = m.getMAxMin(array,0,len(array)-1)
	print("max = ",result[1])
	print("min = ",result[0])