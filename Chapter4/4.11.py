# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 14:40
Project:AlgorithmBook
Filename:4.11.py
"""

"""
如何找出数组中出现1次的数
题目描述：一个数组里，除了三个数是唯一出现的，其余的数都出现偶数次，找出这三个数中的任意一个。
"""

# 判断数字n的二进制数从右到左数第i位是否为1
def isOne(n,i):
	return (n&(1<<i)) == 1

def findSingle(array):
	size = len(array)
	i = 0
	while i < 32:
		result1 = result0 = count1 = count0 = 0
		j = 0
		while j < size:
			if isOne(array[j],i):
				result1 ^= array[j]                     # 第i位为1的值异或操作
				count1 += 1                             # 第i位位1的数字个数
			else:
				result0 ^= array[j]                     # 第i位为0的值异或操作
				count0 += 1                             # 第i位为0的数字个数
			j += 1
		i += 1
		# '''
		# bit值为1是子数组元素个数为奇数，且出现1次的数字被分配到bit值为0的子数组，说明只有一个出现1次的数字
		# 被分配到bit值为1的子数组中，异或记过就是这个出现一次的数字
		# '''
		if count1 % 2 == 1 and result0 != 0:
			return result1
		# 只有一个出现一次的数字被分配到bit值为0的子数组中
		if count0 % 2 == 1 and result1 != 0:
			return result0
	return -1


if __name__ == "__main__":
	array = [6,3,4,5,9,4,3]
	result = findSingle(array)
	if result != -1:
		print(result)
	else:
		print("没有找到")