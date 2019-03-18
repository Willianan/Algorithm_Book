# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/28 14:20
Project:AlgorithmBook
Filename:4.3.py
"""

"""
如何找出旋转数组的最小元素
题目描述：把一个有序数组最开始的若干元素搬到数组的末尾，称之为数组的旋转。输入一个排序好的数组的一旋转，
输出旋转数组的最小元素。
"""

# python中可以使用列表来表示有序数组‘
def getMin_l(array,low,high):
	# 如果旋转个数为0，单独处理，直接返回数组头元素
	if high < low:
		return array[0]
	# 只剩下一个元素一定是最小值
	if high == low:
		return array[low]
	# mid = (low + high) // 2 采用下面写法防止溢出
	mid = low + ((high - low) >> 1)
	# 判断是否array为最小值
	if array[mid] < array[mid - 1]:
		return array[mid]
	# 判断array[mid+1]为最小值
	elif array[mid+1] < array[mid]:
		return array[mid+1]
	# 最小值一定在数组左半部分
	elif array[high] > array[mid]:
		return getMin_l(array,low,mid-1)
	# 最小值一定在数组右半部分
	elif array[mid] > array[low]:
		return getMin_l(array,mid+1,low)
	# 这中情况下无法确定最小值所在位置，需要在左右两部分分别进行查找
	else:
		return min(getMin_l(array,low,mid-1),getMin_l(array,mid+1,high))

def getMin(array):
	if array == None:
		print("数组为空")
		return
	else:
		return getMin_l(array,0,len(array)-1)


if __name__ == "__main__":
	array = [5,6,1,2,3,4]
	mins = getMin(array)
	print(mins)
	array = [1,1,0,1]
	mins = getMin(array)
	print(mins)

"""
引申：如何实现旋转数组功能
"""
def swap(array,low,high):
	# 交换数组low到high的元素
	while low < high:
		tmp = array[low]
		array[low] = array[high]
		array[high] = tmp
		low += 1
		high -= 1

def rotateArray(array,div):
	if array == None or div < 0 or div >= len(array):
		print("参数不合法")
		return
	# 不需要旋转
	if div == 0 or div == len(array) - 1:
		return
	# 交换第一个子数组的元素
	swap(array,0,div)
	# 交换第二子数组的元素
	swap(array,div+1,len(array)-1)
	# 交换整个数组的元素
	swap(array,0,len(array)-1)

if __name__ == "__main__":
	array = [1,2,3,4,5]
	rotateArray(array,2)
	i = 0
	while i < len(array):
		print(array[i],end=' ')
		i += 1