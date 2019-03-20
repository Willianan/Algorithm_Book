# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/14 9:26
Project:AlgorithmBook
Filename:5.16.py
"""

"""
求一个串中出现的第一个最长重复串
 题目描述：给定一个字符串，找出这个字符串中最长的重复子串
 输入：banana
 输出：ana
"""
class CommonSubString:
	# 找出最长的公共子串的长度
	def maxPrefix(self,str1,str2):
		i = 0
		while i < len(str1) and i < len(str2):
			if list(str1)[i] == list(str2)[i]:
				i += 1
			else:
				break
			i += 1
		return i

	def getMaxCommonStr(self,strs):
		# 用来存储后缀数组
		suffixes = [None]*len(strs)
		longestSubStrLen = 0
		longestSubStr = None
		# 获取到后缀数组
		i = 0
		while i < len(strs):
			suffixes[i] = strs[i:]
			i += 1
		# 对后缀数组进行排序
		suffixes.sort()
		i = 1
		while i < len(strs):
			temp = self.maxPrefix(suffixes[i],suffixes[i-1])
			if temp > longestSubStrLen:
				longestSubStrLen = temp
				longestSubStr = suffixes[i][0:i+1]
			i += 1
		return longestSubStr


if __name__ == "__main__":
	strs = "banana"
	c = CommonSubString()
	print("最长的公共子串为：",c.getMaxCommonStr(strs))