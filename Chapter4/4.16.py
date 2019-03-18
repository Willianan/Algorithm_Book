# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 20:09
Project:AlgorithmBook
Filename:4.16.py
"""

"""
如何在有规律的二维数组中进行高效的数据查找
题目描述：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请实现一个函数，输入这样的一个
二维数组和一个整数判断数组中是否含有该整数
"""

def findWithBinary(array,data):
	if array == None or len(array) < 1:
		print("参数不合理")
		return False
	# 从二维数组右上角元素开始遍历
	i = 0
	rows = len(array)
	columns = len(array[0])
	j = columns - 1
	while i < rows and j >= 0:
		# 在数组中找到data
		if array[i][j] == data:
			return True
		# 当前遍历到数组中的值大于data，data肯定不再这一列中
		elif array[i][j] > data:
			j -= 1
		# 当前遍历到数组中的值小于data，data肯定不再这一行中
		else:
			i += 1
	return  False
if __name__ == "__main__":
	array =[[1,2,3,4],
	        [11,12,13,14],
	        [21,22,23,24],
	        [31,32,33,34],
	        [41,42,43,44]]
	print(findWithBinary(array,17))
	print(findWithBinary(array,24))