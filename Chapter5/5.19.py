# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/14 10:31
Project:AlgorithmBook
Filename:5.19.py
"""

"""
如何求字符串的编辑距离
题目描述：编辑距离又称Levenshtein距离，是指两个字符串之间由一个转成另一个所需的最少编辑操作次数。
许可的编辑操作包括一个字符替换成另一个字符、插入一个字符、删除一个字符。请设计并实现一个算法来计算
两个字符串的编辑距离，并计算其复杂度。在某些应用场景下，替换操作的代价比较高，假设替换操作的代价是
插入和删除的两倍。
"""
class EditDistance:
	def mins(self,a,b,c):
		tmp = a if a < b else b
		return tmp if tmp < c else c
	# 参数replaceWight用来表示替换操作与插入删除操作的倍数
	def edit(self,s1,s2,replaceWight):
		# 两个空串的编辑距离为0
		if s1 == None and s2 == None:
			return 0
		# 其中一个为空串，那么编辑距离为另一个字符串的长度
		if s1 == None:
			return len(s2)
		if s2 == None:
			return len(s1)
		# 申请二维数组来存储中间的计算结果
		D = [([None]*(len(s2)+1)) for i in range(len(s1)+1)]
		i = 0
		while i < len(s1)+1:
			D[i][0] = i
			i += 1
		i = 0
		while i < len(s2)+1:
			D[0][i] = i
			i += 1
		i = 1
		while i < len(s1)+1:
			j = 1
			while j < len(s2)+1:
				if list(s1)[i-1] == list(s2)[j-1]:
					D[i][j] = self.mins(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1])
				else:
					D[i][j] = min(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+replaceWight)
				j += 1
			i += 1
		print("------------------------------------")
		i = 0
		while i < len(s1)+1:
			j = 0
			while j < len(s2)+1:
				print(D[i][j],end=' ')
				j += 1
			print()
			i += 1
		print("------------------------------------")
		dis = D[len(s1)][len(s2)]
		return dis
if __name__ == "__main__":
	s1 = "bciln"
	s2 = "fciling"
	ed = EditDistance()
	print("第一问：")
	print("编辑距离为：",str(ed.edit(s1,s2,1)))
	print("第二问：")
	print("编辑距离为：",str(ed.edit(s1,s2,2)))