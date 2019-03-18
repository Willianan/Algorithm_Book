# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/4 9:12
Project:AlgorithmBook
Filename:4.22.py
"""

"""
如何从三个有序数组中找出它们的公共元素
题目描述：给定以非递减顺序排序的三个数组，找出这三个数组中的所有公共元素。
"""
def findCommon(array1,array2,array3):
	i = 0
	j = 0
	k = 0
	# 遍历三个数组
	while i < len(array1) and j < len(array2) and k < len(array3):
		# 找到公共元素
		if array1[i] == array2[j] == array3[k]:
			print(array1[i],end=' ')
			i += 1
			j += 1
			k += 1
		# array1[i]不是公共元素
		elif array1[i] < array2[j]:
			i += 1
		# array2[j]	不是公共元素
		elif array2[j] < array3[k]:
			j += 1
		# array3[k]不是公共元素
		else:
			k += 1


if __name__ == "__main__":
	array1 = [2,5,12,20,45,85]
	array2 = [16,19,20,85,200]
	array3 = [3,4,15,20,39,72,85,190]
	findCommon(array1,array2,array3)