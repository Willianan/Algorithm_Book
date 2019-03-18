# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 15:11
Project:AlgorithmBook
Filename:4.13.py
"""

"""
如何在不排序的情况下求数组中的中位数
题目描述：所谓中位数就是一组数据从小到大排列后中间的那个数字。如果数组长度为偶数，那么中位数的值就是中间两个数字相加
除以2，如果数组长度为奇数，那么中位数的值就是中间那个数字。
"""
class Test:
	def __init__(self):
		self.pos = 0
	# 以array[low]为基准把数组分成两部分
	def partition(self,array,low,high):
		key = array[low]
		while low < high:
			while low < high and array[high] >= key:
				high -= 1
			array[low] = array[high]
			while low < high and array[low] <= key:
				low += 1
			array[high] = array[low]
		array[low] = key
		self.pos = low

	def getMid(self,array):
		low = 0
		high = len(array) - 1
		mid = (low + high) // 2
		while True:
			# array[low]为基准把数组分成两部分
			self.partition(array,low,high)
			if self.pos == mid:                     # 找到中位数
				break
			elif self.pos > mid:                    # 继续在右半部分查找
				high = self.pos - 1
			else:                                   # 继续在左半部分查找
				low = self.pos + 1
		# 如果数组长度为奇数，中位数为中间的元素，否则就是中间两个数的平均值
		return array[mid] if len(array)%2 != 0 else (array[mid] + array[mid+1])/2


if __name__ == "__main__":
	array = [7,5,3,1,11,9]
	result = Test().getMid(array)
	print(result)