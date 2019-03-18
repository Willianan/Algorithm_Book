# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/28 8:17
Project:AlgorithmBook
Filename:4.1.py
"""

"""
如何找出数组中唯一的重复元素
题目描述：数组1~1000放在含有1001个元素的数组中，其中只有唯一的一个元素值重复，其他数字均只出现一次。
设计一个算法，将重复元素找出来，要求每个数组元素只能访问一次且不能使用辅助存储空间。
"""

# 方法一：空间换时间法
'''
**** 方法功能：在数组中找出唯一的重复的元素
**** 输入参数：array：数组对象的引用
**** 返回值：  重复元素的值，如果无重复元素则返回-1
'''

def FindDup1(array):
	if array == None:
		return -1
	length = len(array)
	hashtable = dict()
	i = 0
	while i < length:
		hashtable[i] = 0
		i += 1
	j = 0
	while j < length:
		if hashtable[array[j] - 1] == 0:
			hashtable[array[j] - 1] = array[j] - 1
		else:
			return array[j]
		j += 1
	return -1

# 方法二：累加求和法
# 方法三：异或法
def FindDup3(array):
	if array == None:
		return -1
	length = len(array)
	result = 0
	i = 0
	while i < length:
		result ^= array[i]
		i += 1
	j = 1
	while j < length:
		result ^= j
		j += 1
	return result
# 方法四：数据映射法
def FindDup4(array):
	if array == None:
		return -1
	length = len(array)
	index = 0
	i = 0
	while True:
		# 数组中的元素的值只能小于len，否则会越界
		if array[i] >= length:
			return -1
		if array[index] < 0:
			break
		# 访问过，通过变相反数的方法进行标记
		array[index] *= -1
		# index的后继为array[index]
		index = -1 * array[index]
		if index >= length:
			print("数组中有非法数字")
			return -1
	return index

# 方法五：环形相遇法
def FindDup5(array):
	if array == None:
		return -1
	slow = 0
	fast = 0
	while True:
		fast = array[array[fast]]                   # fast一次走两步
		slow = array[slow]                          # slow一次走一步
		if slow == fast:                            # 找到相遇点
			break
	fast = 0
	while True:
		fast = array[fast]
		slow = array[slow]
		if slow == fast:                            # 找到入口点
			return -slow

if __name__ == "__main__":
	array = [1,3,4,2,5,3]
	print(FindDup1(array))
	print(FindDup3(array))
	print(FindDup4(array))
	print(FindDup5(array))


'''
引申：对于一个给定的自然数Ｎ，有一个Ｎ＋Ｍ个元素的数组，其中存放 小于等于N的所有自然数，求重复出现的自然数序列[X]
'''
def FindDup(array,num):
	s = set()
	if array == None:
		return s
	length = len(array)
	index = array[0]
	num = num - 1
	while True:
		if array[index] < 0:
			num -= 1
			array[index] = length - num
			s.add(index)
		if num == 0:
			return s
		array[index] *= -1
		index = array[index] *(-1)


if __name__ == "__main__":
	array = [1,2,3,3,3,4,5,5,5,5,6]
	num = 6
	s = FindDup(array,num)
	for i in s:
		print(i,end=' ')