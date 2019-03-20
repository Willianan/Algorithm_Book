# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/14 9:49
Project:AlgorithmBook
Filename:5.17.py
"""

"""
如何求解字符串中字典序最大的子序列
题目描述：给定一个字符串，求串中字典最大的子序列。字典最大的序列是这样构造的：给定字符串a0a1···an-1,
首先在字符串a0a1···an-1中找到最大的字符ai,然后在剩余的字符串ai+1···an-1中找到值最大的字符aj,然后在
剩余的aj+1···an-1中找到值最大的字符ak,···直到字符串的长度为0，则aiajak···即为答案。
"""
# 方法一：顺序遍历法
def getLargestSub(src):
	if src == None:
		return None
	largestSub = [None]*(len(src)+1)
	k = 0
	i = 0
	while i < len(src):
		largestSub[k] = list(src)[i]
		j = i + 1
		while j < len(src):
			# 找出第i个字符后面最大的字符放到largestSub[k]中
			if list(src)[j] > largestSub[k]:
				largestSub[k] = list(src)[j]
				i = j
			j += 1
		k += 1
		i += 1
	return ''.join(largestSub[0:k])

# 方法二：逆序遍历法
def getLargestSub2(str):
	if str == None:
		return None
	largestSub = [None]*(len(str)+1)
	# 最后一个字符一定在子串中
	largestSub[0] = list(str)[len(str)-1]
	i = len(str) - 2
	j = 0
	# 逆序遍历字符串
	while i > 0:
		if ord(list(str)[i]) >= ord(largestSub[j]):
			j += 1
			largestSub[j] = list(str)[i]
		i -= 1
	largestSub = largestSub[0:j+1]
	# 对子串进行逆序
	i = 0
	while i < j:
		temp = largestSub[i]
		largestSub[i] = largestSub[j]
		largestSub[j] = temp
		i += 1
		j -= 1
	return ''.join(largestSub)
if __name__ == "__main__":
	s = "acbxmng"
	result = getLargestSub(s)
	if result == None:
		print("字符串为空")
	else:
		print(result)
	result = getLargestSub2(s)
	if result == None:
		print("字符串为空")
	else:
		print(result)