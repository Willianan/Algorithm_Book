# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/11 9:54
Project:AlgorithmBook
Filename:5.9.py
"""

"""
如何实现字符串的匹配
题目描述:给定主字符串S与模式字符串P，判断P是否是S的子串，如果是，那么找出P在S中第一次出现的下标
"""

# 方法一：直接计算法
'''
***** 方法功能：判断p是否是s的子串，如果是返回p在s中第一次出现的下标，否则返回-1
***** 输入参数：s和p分别为主串和模式串
'''
def match(s,p):
	# 检查参数是否合理
	if s == None or p == None:
		print("参数不合理")
		return -1
	slength = len(s)
	plength = len(p)
	# p肯定不是s的子串
	if slength < plength:
		return -1
	i = 0
	j = 0
	while i < slength and j < plength:
		if list(s)[i] == list(p)[j]:
			# 如果相同，那么继续比较后面的字符
			i += 1
			j += 1
		else:
			# 后退回去重新比较
			i = i - j + 1
			j = 0
			if i > (slength - plength):
				return -1
	if j >= plength:            # 匹配成功
		return i - plength
	return -1

if __name__ == "__main__":
	s = "xyzsabcd"
	p = "abc"
	print(match(s,p))


