# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 15:00
Project:AlgorithmBook
Filename:4.12.py
"""

"""
如何对数组旋转
题目描述：print_rotate_matrix(intmatrix,int n),该方法用于将一个n*n的二维数组逆时针旋转45°后打印
"""

def rotateArray(array):
	i = len(array) - 1
	while i > 0:
		row = 0
		col = i
		while col < len(array):
			print(array[row][col],end=' ')
			row += 1
			col += 1
		print()
		i -= 1
	i = 0
	while i < len(array):
		row = i
		col = 0
		while row < len(array):
			print(array[row][col],end=' ')
			row += 1
			col += 1
		print()
		i += 1


if __name__ == "__main__":
	array = [[1,2,3],[4,5,6],[7,8,9]]
	rotateArray(array)