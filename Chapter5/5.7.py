# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/6 10:57
Project:AlgorithmBook
Filename:5.7.py
"""

"""
如何消除字符串的内嵌括号
题目描述：给定一个如下格式的字符串：(1,(2,3),(4,(5,6),7),括号内的元素可以是数字，也可以是另一个括号，
实现一个算法消除嵌套的括号。
"""
def removeNestedPare(str):
	if str == None:
		return
	Parentheses_num = 0                 # 用来记录不匹配的"("出现的次数
	if list(str)[0] != '(' or list(str)[-1] != ')':
		return None
	sb ='('
	# 字符串首尾的括号可以单独处理
	i = 1
	while i < len(str)-1:
		ch = list(str)[i]
		if ch == '(':
			Parentheses_num += 1
		elif ch == ')':
			Parentheses_num -= 1
		else:
			sb = sb + (list(str)[i])
		i += 1
	# 判断括号是否匹配
	if Parentheses_num != 0:
		print("由于括号不匹配，因此不做任何操作")
		return None
	# 处理字符串结尾的")"
	sb = sb +')'
	return sb

if __name__ == "__main__":
	str = "(1,(2,3),(4,(5,6),7))"
	print(str+"去除嵌套括号后为：",removeNestedPare(str))