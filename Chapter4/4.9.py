# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 10:27
Project:AlgorithmBook
Filename:4.9.py
"""

"""
如何求数组中绝对值最小的数
题目描述：有一个升序的数组，数组中可能有正数、负数或0，求数组中元素的绝对值最小的数
"""

# 方法一：顺序比较法
def FindMin1(array):
	if array == None or len(array)< 1:
		print("数组不存在")
		return 0
	mins = 2**32
	i = 0
	while i < len(array):
		if abs(array[i] < abs(mins)):
			mins = array[i]
		i += 1
	return mins

# 方法二：二分法
def FindMin2(array):
	if array == None or len(array) < 1:
		print("数组不存在")
		return 0
	# 数组中没有负数
	if array[0] >= 0:
		return array[0]
	# 数组中没有正数
	if array[len(array)-1] <= 0:
		return array[len(array)-1]
	mid = 0
	begin = 0
	end = len(array) - 1
	absMin = 0
	#数组中既有正数也有负数
	while True:
		mid = begin + (end - begin) // 2
		# 如果等于0，那么就是绝对值最小的数
		if array[mid] == 0:
			return 0
		# 如果大于0，正负数的分界点在左侧
		elif array[mid] > 0:
			# 继续在数组的左半部分查找
			if array[mid-1] > 0:
				end = mid - 1
			elif array[mid] == 0:
				return 0
			else:
				break
		# 如果小于0，在数组右半部分查找
		else:
			if array[mid+1] < 0:
				begin = mid + 1
			elif array[mid+1] == 0:
				return 0
			else:
				break
	# 获取正负数分界点处绝对值最小的值
	if array[mid] > 0:
		if array[mid] < abs(array[mid-1]):
			absMin = array[mid]
		else:
			absMin = array[mid-1]
	else:
		if array[mid] < array[mid+1]:
			absMin = array[mid]
		else:
			absMin = array[mid+1]
	return absMin



if __name__ == "__main__":
	array = [-10,-5,-2,7,15,50]
	print("绝对值最小的数为：",FindMin1(array))
	print("绝对值最小的数为：",FindMin2(array))