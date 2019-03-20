# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/6 9:57
Project:AlgorithmBook
Filename:5.4.py
"""

"""
如何判断两个字符串是否为换位字符串
题目描述：换位字符串是指组成字符串的字符相同，但位置不同。
"""

'''
***** 方法功能：判断两个字符串是否为换位字符串
***** 输入参数：s1和s2为两个字符串
***** 返回值：  如果是返回True，否则返回False
'''

def compare(s1,s2):
	result = True
	bCount = [None]*256
	i = 0
	while i < 256:
		bCount[i] = 0
		i += 1
	i = 0
	while i < len(s1):
		bCount[ord(list(s1)[i])-ord('0')] += 1
		i += 1
	i = 0
	while i < len(s2):
		bCount[ord(list(s2)[i]) - ord('0')] -= 1
		i += 1
	i = 0
	while i < 256:
		if bCount[i] != 0:
			result = False
			break
		i += 1
	return result



if __name__ == "__main__":
	str1 = "aaaabbc"
	str2 = "abcabaa"
	print(str1+"和"+str2,end='')
	if compare(str1,str2):
		print("是换位字符")
	else:
		print("不是换位字符")