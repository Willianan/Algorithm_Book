# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/12 10:46
Project:AlgorithmBook
Filename:5.14.py
"""

"""
如何统计字符串中连续的重复字符个数
题目描述：用递归的方法实现一个求字符串中连续出现相同字符的最大值。
"""

def getMaxDupChar(s,startIndex,curMaxLen,maxLen):
	# 字符串遍历结束，返回最长连续重复字符串的长度
	if startIndex == len(s)-1:
		return max(curMaxLen,maxLen)
	# 如果两个连续的字符相等，那么在递归调用的时候把当前最长的长度加1
	if list(s)[startIndex] == list(s)[startIndex+1]:
		return getMaxDupChar(s,startIndex+1,curMaxLen+1,maxLen)
	# 两个连续的子串不想等，求出最长串max(curMaxLen,maxLen)
	# 当前连续重复字符串的长度变为1
	else:
		return getMaxDupChar(s,startIndex+1,1,max(curMaxLen,maxLen))

if __name__ ==  "__main__":
	print("abbc的最长连续重复子串长度为：",getMaxDupChar("abbc",0,1,1))
	print("aaabbccdddddd的最长连续重复子串长度为：",getMaxDupChar("aaabbccdddddd",0,1,1))