# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/5 10:21
Project:AlgorithmBook
Filename:5.2.py
"""

"""
如何求字符串的最长公共子串
题目描述：找出两个字符串的最长公共子串。
"""
# 方法一：动态规划法
'''
***** 方法功能：获取两个字符串的最长公共子串
***** 输入参数：str1和str2为指向字符的指针
'''
def getMaxSubStr(str1,str2):
	len1 = len(str1)
	len2 = len(str2)
	sb = ''
	maxs = 0
	maxI = 0
	# 申请新的空间来记录公共字串长度信息
	M = [[0 for i in range(len1+1)] for j in range(len2+1)]
	# 通过利用递归公式填写新建的二维数组（公共字串的长度信息）
	i = 0
	while i < len1+1:
		M[i][0] = 0
		i += 1
	j = 0
	while j < len2+1:
		M[0][j] = 0
		j += 1
	i = 1
	while i < len1+1:
		j = 1
		while j < len2+1:
			if list(str1)[i-1] == list(str2)[j-1]:
				M[i][j] = M[i-1][j-1] + 1
				if M[i][j] > maxs:
					maxs = M[i][j]
					maxI = i
			else:
				M[i][j] = 0
			j += 1
		i += 1
	# 找出公共字串
	i = maxI - maxs
	while i < maxI:
		sb = ''.join(list(str1)[i])
		i += 1
	return sb


if __name__ == "__main__":
	str1 = "abcade"
	str2 = "dgcadde"
	print(getMaxSubStr(str1,str2))