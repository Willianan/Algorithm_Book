# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 15:52
Project:AlgorithmBook
Filename:4.14.py
"""

"""
如何求集合的所有子集
题目描述：有一个集合，求其全部子集(包含集合自身)。给定一个集合s，它包含两个元素<a,b>，则其全部的子集为<a,ab,b>
"""
# 方法一：位图法
def getAllSubset1(array,mask,c):
	if len(array) == c:
		print("{",end=' ')
		i = 0
		while i < len(array):
			if mask[i] == 1:
				print(array[i],end=' ')
			i += 1
		print("}",end='')
		print()
	else:
		mask[c] = 1
		getAllSubset1(array,mask,c+1)
		mask[c] = 0
		getAllSubset1(array,mask,c+1)

# 方法二：迭代法
def getAllSubset2(str):
	if str == None or len(str) < 1:
		print("参数不合理")
		return  None
	array = []
	array.append(str[0:1])
	i = 1
	while i < len(str):
		j = 0
		while j < len(str):
			array.append(array[j]+str[i])
			j += 1
		array.append(str[i:i+1])
		i += 1
	return array



if __name__ == "__main__":
	array = ['a','b','c']
	mask = [0,0,0]
	getAllSubset1(array,mask,0)
	result = getAllSubset2('abc')
	i = 0
	while i < len(result):
		print(result[i])
		i += 1