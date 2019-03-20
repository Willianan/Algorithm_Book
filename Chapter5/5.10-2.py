# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/11 11:13
Project:AlgorithmBook
Filename:5.10-2.py
"""

# 中心扩展法
class Test:
	def __init__(self):
		self.startIndex = None
		self.lens = 0
	def getStartIndex(self):
		return self.startIndex
	def getLens(self):
		return self.lens
	# 对字符串str，以c1和c2为中心向两侧扩展寻找回文字符串
	def expandBothSide(self,strs,c1,c2):
		n = len(strs)
		while c1 >= 0 and c2 < n and list(strs)[c1] == list(strs)[c2]:
			c1 -= 1
			c2 += 1
		tmpStartIndex = c1 + 1
		tmpLen = c2 - c1 - 1
		if tmpLen > self.lens:
			self.lens = tmpLen
			self.startIndex = tmpStartIndex
	# 方法功能：找出字符串最长的回文子串
	def getLongestPalindrome(self,strs):
		if strs == None:
			return
		n = len(strs)
		if n < 1:
			return
		i = 0
		while i < n-1:
			# 找回文子串长度为奇数的情况
			self.expandBothSide(strs,i,i)
			# 找回文子串长度为偶数的情况
			self.expandBothSide(strs,i,i+1)
			i += 1

if __name__ == "__main__":
	strs = "abcdefgfedxyz"
	t = Test()
	t.getLongestPalindrome(strs)
	if t.getStartIndex() != -1 and t.getLens() != -1:
		print("最长的回文字符串为：",end='')
		i = t.getStartIndex()
		while i < t.getStartIndex()+t.getLens():
			print(list(strs)[i],end='')
			i += 1
	else:
		print("查找失败")