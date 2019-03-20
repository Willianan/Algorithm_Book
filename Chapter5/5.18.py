# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/14 10:16
Project:AlgorithmBook
Filename:5.18.py
"""

"""
如何判断一个字符串是否由另外一个字符串旋转得到
题目描述：给定一个能判断一个单词是否为另外一个单词的子字符串的方法，记为isSubstring。如何判断
s2是否能通过旋转s1得到（只能使用一次isSubstring方法）
input:waterbottle
output:erbottlewat
"""
# 函数功能：判断str2是否为str1的子串
def isSubString(str1,str2):
	return str1.find(str2) != -1
# 函数功能：判断str2是否可以通过旋转str1得到
def rotateSame(str1,str2):
	if str1 == None or str2 == None:
		return False
	# 判断两个字符串长度是否相等，如果不相等，那么不可能通过旋转得到
	if len(str1) != len(str2):
		return False
	# 申请临时空间存储str1str1.多申请一个空间存储'\0'
	tmp  = [None]*(2*len(str1)+1)
	i = 0
	while i < len(str1):
		tmp[i] = list(str1)[i]
		tmp[i+len(str1)] = list(str1)[i]
		i += 1
	tmp[2*len(str1)] = '\0'
	# 判断str2是否为tmp的子串
	result = isSubString(''.join(tmp),str2)
	return result

if __name__ == "__main__":
	str1 = "waterbottle"
	str2 = "erbottlewat"
	result = rotateSame(str1,str2)
	if result:
		print(str2+"可以通过旋转"+str1+"得到")
	else:
		print(str2+"不可以通过旋转"+str1+"得到")