# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019/3/20 9:27
@Project:AlgorithmBook
@Filename:7.7.py
"""

"""
如何判断还有几盏灯泡亮着
题目描述：100个灯泡排成一排，第一轮将所有的灯泡打；第二轮每隔一个灯泡关掉一个，即排在偶数
的灯泡被关掉；第三轮每隔两个灯泡，将开着的灯泡关掉，关掉的灯泡打开。依此类推，第100轮结束
的时候，还有几盏灯跑亮着？
"""
def factorIsOdd(a):
	total = 0
	i = 1
	while i <= a:
		if a%i == 0:
			total += 1
		i += 1
	if total%2 == 1:
		return 1
	else:
		return 0

def totalCount(num,n):
	count = 0
	i = 0
	while i < n:
		# 判断因子数是否为奇数，如果是奇数（灯亮），那么加1
		if factorIsOdd(num[i]) == 1:
			print("亮着的灯的编号为：",num[i])
			count += 1
		i += 1
	return count


if __name__ == "__main__":
	num = [None] * 100
	i = 0
	while i < 100:
		num[i] = i + 1
		i += 1
	count = totalCount(num,100)
	print("最后总共有"+str(count)+"盏灯亮着。")