# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/12 10:13
Project:AlgorithmBook
Filename:5.13.py
"""

"""
如何找到其单词组成的最长单词
题目描述：给定一个字符串数组，找出数组中最长的字符串，使其能由数组中其他的字符串组成。
"""

class LongestWord:
	def find(self,strArray,strs):
		i = 0
		while i < len(strArray):
			if strs == strArray[i]:
				return True
			i += 1
		return False
	'''
	***** 方法功能：判断字符串word是否能由数组strArray中的其他单词组成
	***** 输入参数：word：待判断的后缀子串；length:待判断字符串的长度
	'''
	def isContain(self,strArray,word,length):
		# 递归的结束条件，当字符串长度为0，说明字符串已经遍历完了
		if len(word) == 0:
			return True
		# 循环取字符串的所有前缀
		i = 1
		while i <= len(word):
			# 取到的子串为自己
			if i == length:
				return False
			strs = word[0:i]
			if self.find(strArray,strs):
				# 查找完字符串的前缀后，递归判断后面的子串能否由其他单词组成
				if self.isContain(strArray,word[i:],length):
					return True
			i += 1
		return False
	# 方法功能：找出能由数组中其他字符串组成的最长字符串
	def getLongestStr(self,strArray):
		# 对字符串由大到小排序
		strArray = sorted(strArray,reverse=True)
		print(strArray)
		# 贪心地从最长的字符串开始判断
		i = 0
		while i < len(strArray):
			if self.isContain(strArray,strArray[i],len(strArray[i])):
				return strArray[i]
			i += 1
		# 如果没有找到，那么返回空串
		return None


if __name__ == "__main__":
	strArray = ["test","tester","testertest","testing","apple","seattle","banana","batting",
	            "ngcat","batti","bat","testingtester","testbattingcat"]
	lw = LongestWord()
	longestStr = lw.getLongestStr(strArray)
	if longestStr != None:
		print("最长的字符串为："+longestStr)
	else:
		print("不存在这样的字符串")