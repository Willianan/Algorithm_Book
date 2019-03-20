# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/12 9:15
Project:AlgorithmBook
Filename:5.11.py
"""

"""
如何按照给定的字母序列对字符数组排序
题目描述：已知字母序列[d,g,e,c,f,b,o,a]，请实现一个方法，要求对输入的一组字符串input=["bed","dog","dear","eye"]
按照字母顺序排列并打印。
"""
# 根据char_to_int给定的字符的大小比较两个字符的大小
def compare(str1,str2,char_to_int):
	len1 = len(str1)
	len2 = len(str2)
	i = 0
	j = 0
	while i < len1 and j < len2:
		# 如果字符不再给定的序列中，那么把值赋为-1
		if list(str1)[i] not in char_to_int.keys():
			char_to_int[list(str1)[i]] = -1
		if list(str2)[j] not in char_to_int.keys():
			char_to_int[list(str2)[j]] = -1
		# 比较各个字符的大小
		if char_to_int[list(str1)[i]] < char_to_int[list(str2)[j]]:
			return -1
		elif char_to_int[list(str1)[i]] > char_to_int[list(str2)[j]]:
			return 1
		else:
			i += 1
			j += 1
	if i == len1 and j == len2:
		return 0
	elif i == len1:
		return -1
	else:
		return 1

def insertSort(s,char_to_int):
	# 对字符串数组进行排序
	lens = len(s)
	i = 1
	while i < lens:
		temp = s[i]
		j = i -1
		while j >= 0:
			# 用给定的规则比较字符串的大小
			if compare(temp,s[j],char_to_int) == -1:
				s[j+1] = s[j]
			else:
				break
			j -= 1
		s[j+1] = temp
		i += 1


if __name__ == "__main__":
	s = ["bed","dog","dear","eye"]
	sequence = "dgecfboa"
	lens = len(sequence)
	# 用来存储字母序列与其对应的值的键值对
	char_to_int = dict()
	# 根据给定的字符序列构造字典
	i = 0
	while i < lens:
		char_to_int[list(sequence)[i]] = i
		i += 1
	insertSort(s,char_to_int)
	i = 0
	while i < len(s):
		print(s[i],end=' ')
		i += 1