# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/28 15:30
Project:AlgorithmBook
Filename:4.5.py
"""

"""
如何找出数组中出现奇数次的数
题目描述：数组中有N+2个数，其中，N个数出现了偶数次，2个数出现了奇数次(这两个数不想等)，
请用O(1)的空间复杂度找出这两个数。
注意：不需要知道具体位置，只需要找出这两个数
"""

#方法一：字典法
def get2Num1(array):
	if array == None or len(array) < 1:
		print("参数不合理")
		return
	dictions = dict()
	i = 0
	while i < len(array):
		# dictions中没有这个数字，说明第一次出现，value赋值为1
		if array[i] not in dictions:
			dictions[array[i]] = 1
		# 当前遍历的值在dictions中存在，说明前面出现过，value赋值为0
		else:
			dictions[array[i]] = 0
		i += 1
	for k,v in dictions.items():
		if v == 1:
			print(int(k),end=' ')

# 方法二：异或法
def get2Num2(array):
	if array == None or len(array) < 1:
		print("参数不合理")
		return
	result = 0
	position = 0
	# 计算数组中所有数字异或的结果
	i = 0
	while i < len(array):
		result = result ^ array[i]
		i += 1
	tmpResult = result         # 临时保存异或结果
	# 找出异或结果中其中一个位值为1的位数(如1100 位值为1位数为2和3)
	i = result
	while i & 1 == 0:
		position += 1
		i = i >> 1
	i = 1
	while i < len(array):
		# 异或的结果与所有第position位为1的数异或，结果与i的是出现一次的两个数中其中一个
		if ((array[i] >> position) & 1) == 1:
			result = result ^ array[i]
		i += 1
	print(result,end=' ')
	# 得到另外一个出现一次的数
	print(result^tmpResult,end=' ')


if __name__ == "__main__":
	array = [3,5,6,6,5,7,2,2]
	get2Num1(array)
	print()
	get2Num2(array)