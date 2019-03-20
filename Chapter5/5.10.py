# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/11 10:51
Project:AlgorithmBook
Filename:5.10.py
"""

'''
如何求字符串里的最长回文子串
题目描述：回文字符串是指一个字符串从左到右遍历得到的序列是相同的
'''
# 方法一：动态规划法
class Test:
	def __init__(self):
		self.startIndex = None
		self.lens = None
	def getStartIndex(self):
		return self.startIndex
	def getLens(self):
		return self.lens
	# '''
	# ***** 方法功能：找出字符串中最长的回文子串
	# ***** 输入参数：str为字符串，startIndex与lens为找到的回文字符串的起始位置与长度
	# '''
	def getLongesdPalindrome(self,strs):
		if strs == None:
			return
		if len(strs) < 1:
			return
		self.startIndex = 0
		self.lens = 1
		# 申请额外的存储空间记录查找的历史信息
		historyRecord = [([None]*len(strs)) for i in range(len(strs))]
		i = 0
		while i < len(strs):
			j = 0
			while j < len(strs):
				historyRecord[i][j] = 0
				j += 1
			i += 1
		# 初始化长度为1的回文字符串信息
		i= 0
		while i < len(strs):
			historyRecord[i][i] = 1
			i += 1
		# 初始化长度为2的回文字符串信息
		i = 0
		while i < len(strs)-1:
			if list(strs)[i] == list(strs)[i+1]:
				historyRecord[i][i+1] = 1
				self.startIndex = i
				self.lens = 2
			i += 1
		# 查找长度为3开始的回文字符串
		pLen = 3
		while pLen <= len(strs):
			i = 0
			while i < len(strs)-pLen+1:
				j = i+pLen-1
				if list(strs)[i] == list(strs)[j] and historyRecord[i+1][j-1] == 1:
					historyRecord[i][j] = 1
					self.startIndex = i
					self.lens = pLen
				i += 1
			pLen += 1

if __name__ == "__main__":
	strs = "abcdefgfedxyz"
	t = Test()
	t.getLongesdPalindrome(strs)
	if t.getStartIndex() != -1 and t.getLens() != -1:
		print("最长的回文字符串为：",end='')
		i = t.getStartIndex()
		while i < t.getStartIndex()+t.getLens():
			print(list(strs)[i],end='')
			i += 1
	else:
		print("查找失败")