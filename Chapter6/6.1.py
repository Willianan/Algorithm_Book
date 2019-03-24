# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/15 11:02
Project:AlgorithmBook
Filename:6.1.py
"""

"""
如何判断一个自然数是否是某个数的平方
题目描述：判断给定是一个数n是否是某个数的平方，不能使用开方运算。
"""
# 方法一：直接计算法
def isPower(n):
	if n <= 0:
		print(str(n)+"不是自然数")
		return False
	i = 1
	while i < n:
		m = i * i
		if m == n:
			return True
		elif m > n:
			return False
		i += 1
	return False


# 方法二:二分查找法
def isPower2(n):
	low = 1
	high = n
	while low < high:
		mid = (low + high) // 2
		power = mid * mid
		#接着在1~mid-1区间查找
		if power < n:
			low = mid + 1
		else:
			return True
	return False

# 方法三：减法运算法
def isPower3(n):
	minus = 1
	while n > 0:
		n = n - minus
		# n是某个数的平方
		if n == 0 :
			return True
		# n不是某个数的平方
		elif n < 0:
			return False
		# 每次减数都加2
		else:
			minus += 2
	return False

if __name__ == "__main__":
	n1 = 15
	n2 = 16
	if isPower(n1):
		print(str(n1)+"是某个自然数的平方")
	else:
		print(str(n1)+"不是某个自然数的平方")
	if isPower(n2):
		print(str(n2)+"是某个自然数的平方")
	else:
		print(str(n2)+"不是某个自然数的平方")
	print()
	if isPower2(n1):
		print(str(n1)+"是某个自然数的平方")
	else:
		print(str(n1)+"不是某个自然数的平方")
	if isPower2(n2):
		print(str(n2)+"是某个自然数的平方")
	else:
		print(str(n2)+"不是某个自然数的平方")
	print()
	if isPower3(n1):
		print(str(n1)+"是某个自然数的平方")
	else:
		print(str(n1)+"不是某个自然数的平方")
	if isPower3(n2):
		print(str(n2)+"是某个自然数的平方")
	else:
		print(str(n2)+"不是某个自然数的平方")