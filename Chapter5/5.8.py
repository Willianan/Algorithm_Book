# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/6 11:11
Project:AlgorithmBook
Filename:5.8.py
"""

"""
如何判断字符串是否是整数
题目描述：检查字符串是否是整数，如果是整数，那么返回其整数值
"""
# 方法一：递归法
class Test:
	def __init__(self):
		self.flag = None
	def getFlag(self):
		return self.flag
	# 判断c是否是数字，如果是返回True,否则返回False
	def isNumber(self,c):
		return c >= '0' and c <= '9'
	# '''
	# 判断str是否为数字，如果是返回数字，且设置flag=True，否则设置flag=False’
	# 输入参数；str:字符数组；length:数组长度；flag：表示str是否是数字
	# '''
	def strtoint(self,str,length):
		if length > 1:
			if not self.isNumber(list(str)[length-1]):
				# 不是数字
				print("不是数字")
				self.flag = False
				return -1
			if list(str)[0] == '-':
				return self.strtoint(str,length-1)*10-(ord(list(str)[length-1])-ord('0'))
			else:
				return self.strtoint(str,length-1)*10+ord(list(str)[length-1])-ord('0')
		else:
			if list(str)[0] == '-':
				return 0
			else:
				if not self.isNumber(list(str)[0]):
					print("不是数字")
					self.flag = False
					return -1
				return ord(list(str)[0]) - ord('0')
	def strToint(self,s):
		if s == None or len(s) <= 0 or list(s)[0]=='-' and len(s) == 1:
			print("不是数字")
			self.flag = False
			return -1
		if list(s)[0] == '+':
			return self.strtoint(s[1:len(s)],len(s)-1)
		else:
			return self.strtoint(s,len(s))


if __name__ == "__main__":
	t = Test()
	s = "-543"
	print(t.strToint(s))
	s = "534"
	print(t.strToint(s))
	s = "+543"
	print(t.strToint(s))
	s = "++43"
	result = t.strToint(s)
	if t.getFlag():
		print(result)
