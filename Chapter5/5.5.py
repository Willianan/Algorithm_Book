# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/6 10:12
Project:AlgorithmBook
Filename:5.5.py
"""

"""
如何判断两个字符串的包含关系
题目描述：给定有字母组成的字符串s1和s2，其中，s2中的字母的个数不少于s1，如何判断s1是否包含s2？即出现在
s2中的字符在s1中都存在。
"""
# 方法一：直接法
def isContain(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	# 字符串ch1和ch2短
	if len1 < len2:
		i = 0
		while i < len1:
			j = 0
			while j < len2:
				if list(s1)[i] == list(s2)[j]:
					break
				j += 1
			if j >= len2:
				return False
			i += 1
	else:
		# 字符串ch1比ch2长
		i = 0
		while i <len2:
			j = 0
			while j < len1:
				if list(s1)[j] == list(s2)[i]:
					break
				j += 1
			if j >= len1:
				return False
			i += 1
	return True


# 方法二：空间交换时间法
def IsContain(str1,str2):
	k = 0                               # 字母对应数组的下标
	# 使用记录52个大小写字母的出现情况
	flag = [None]*52
	i = 0
	while i < 52:
		flag[i] = 0
		i += 1
	count = 0                           # 记录段字符串中不同字符出现的个数
	len1 = len(str1)
	len2 = len(str2)
	# shortStr,longStr 分别用来记录较短和较长的字符串
	# maxLen,minLen  分别用来记录较长和较短字符的长度
	if len1 < len2:
		shortStr = str1
		minLen = len1
		longStr = str2
		maxLen = len2
	else:
		shortStr = str2
		minLen = len2
		longStr = str1
		maxLen = len1
	# 遍历短字符串
	i = 0
	while i < minLen:
		# 把字符转换成数组对应的下标（大写字母：0~25，小写字母：26~51）
		if ord(list(shortStr)[i]) >= ord('A') and ord(list(shortStr)[i]) <= ord('Z'):
			k = ord(list(shortStr)[i]) - ord('A')
		else:
			k = ord(list(shortStr)[i]) - ord('a') + 26
			if flag[k] == 0:
				flag[k] = 1
				count += 1
			i += 1
	# 遍历长字符串
	j = 0
	while i < maxLen:
		# 把字符转换成数组对应的下标（大写字母：0~25，小写字母：26~51）
		if ord(list(longStr)[j]) >= ord('A') and ord(list(longStr)[j]) <= ord('Z'):
			k = ord(list(longStr)[j]) - ord('A')
		else:
			k = ord(list(longStr)[j]) - ord('a') + 26
			if flag[k] == 1:
				flag[k] = 0
				count -= 1
				if count == 0:
					return True
			j += 1
	return False

if __name__ == "__main__":
	str1 = "abcdef"
	str2 = "acf"
	print(str1+"与"+str2,end='')
	if isContain(str1,str2):
		print("有包含关系")
	else:
		print("没有包含关系")
	print(str1 + "与" + str2, end='')
	if IsContain(str1,str2):
		print("有包含关系")
	else:
		print("没有包含关系")