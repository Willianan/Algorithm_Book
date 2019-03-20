# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/11 12:36
Project:AlgorithmBook
Filename:5.10-3.py
"""

# 方法三：Manacher算法
class Test:
	def __init__(self):
		self.center = None
		self.palindromeLens = 0
	def getCenter(self):
		return self.center
	def getLens(self):
		return self.palindromeLens
	def mins(self,a,b):
		return b if a > b else a
	'''
	****** 方法功能：找出字符串最长的回文子串
	****** 输入参数：str：字符串，center：回文字符的中心字符；len：回文字符串长度
	如果长度为偶数，那么表示中间偏左的那个字符的位置
	'''
	def Manacher(self,str):
		lens = len(str)
		newLen = 2*lens+1
		s = [None]*newLen                   # 插入分隔符后的字符串
		p = [None]*newLen
		id = 0                              # 以第id个字符为中心是回文字符串最右端的下标最大
		i= 0
		while i < newLen:
			# 构造填充字符串
			s[i] = '*'
			p[i] = 0
			i += 1
		self.center = -1
		self.palindromeLens = -1
		# 求解p数组
		i = 1
		while i < newLen:
			if id + p[id] > i:
				p[i] = self.mins(id+p[id]-i,p[2*id-i])
			else:
				p[i] = 1
			# 然后接着向左右两端扩展求最长的回文子串
			while i +p[i] < newLen and i - p[i] > 0 and s[i-p[i]] == s[i+p[i]]:
				p[i] += 1
			# 当前求出的回文字符串最右端的下标更大
			if i + p[i] > id + p[id]:
				id = i
			# 当前求出的回文字符串更长
			if p[i] - 1 > self.palindromeLens:
				self.center = (i+1)//2 -1
				self.palindromeLens = p[i] - 1    # 更新最长回文子串的长度
			i += 1

if __name__ == "__main__":
	strs = "abcbax"
	t = Test()
	t.Manacher(strs)
	center = t.getCenter()
	palindromeLen = t.getLens()
	if center != -1 and palindromeLen != -1:
		print("最长的回文子串为：",end='')
		# 回文子串长度为奇数
		if palindromeLen % 2 == 1:
			i = center - palindromeLen//2
			while i <= center+palindromeLen//2:
				print(list(strs)[i],end='')
				i += 1
		else:
			i = center - palindromeLen//2
			while i < center+palindromeLen//2:
				print(list(strs)[i],end='')
				i += 1
	else:
		print("查找失败")
