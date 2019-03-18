# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 9:21
Project:AlgorithmBook
Filename:4.8.py
"""

"""
如何求解最小三元组距离
题目描述：已知三个升序整数数组a[l],b[m]和c[n]，请在三个数组中各找出一个元素，使得组成的三元组距离最小。
三元组距离的定义是：假设a[i]、b[j]和c[k]是一个三元组，那么距离为：Distance=max(|a[i]-b[j]|,|a[i]-c[k]|,|b[j]-c[k]|)
请设计一个求最小三元组距离的最优算法。
"""

# 方法一：蛮力法
def maxs(a,b,c):
	Maxs = b if a < b else a
	Maxs = c if Maxs < c else Maxs
	return Maxs

def MinDistance1(a,b,c):
	aLen = len(a)
	bLen = len(b)
	cLen = len(c)
	minDist = maxs(abs(a[0]-b[0]),abs(a[0]-c[0]),abs(b[0]-c[0]))
	dist = 0
	i = 0
	while i < aLen:
		j = 0
		while j < bLen:
			k = 0
			while k < cLen:
				dist = maxs(abs(a[i]-b[j]),abs(a[i]-c[k]),abs(b[j]-c[k]))
				# 找出最小距离
				if minDist > dist:
					minDist = dist
				k += 1
			j  += 1
		i += 1
	return minDist


# 方法二：最小距离法
def mins(a,b,c):
	mins = a if a < b else b
	mins = mins if mins < c else c
	return mins

def MinDistance2(a,b,c):
	curDist = 0
	minsd = 0
	minDist = 2**32
	i = 0                       # 数组a的下标
	j = 0                       # 数组b的下标
	k = 0                       # 数组c的下标
	while True:
		curDist = maxs(abs(a[i] - b [j]),abs(a[i] - c[k]),abs(b[j] - c [k]))
		if curDist < minDist:
			minDist = curDist
		# 找出当前遍历到三个数组中的最小值
		minsd = mins(a[i],b[j],c[k])
		if minsd == a[i]:
			i += 1
			if i >= len(a):
				break
		elif minsd == b[j]:
			j += 1
			if j >= len(b):
				break
		else:
			k += 1
			if k >= len(c):
				break
	return minDist


# 方法三：数学运算法
def MinDistance3(a,b,c):
	MinSum = 0                          # 最小的绝对值和
	Sum = 0                             # 计算三个绝对值的和，与最小做比较
	MinOFabc = 0                        # a[i],b[j]，c[k]的最小值
	cnt = 0                             # 循环次数统计，最多是1+m+n次
	i = j = k = 0
	MinSum = (abs(a[i]-b[j])+abs(a[i]-c[k])+abs(b[j]-c[k])) // 2
	while cnt <= len(a)+len(b)+len(c):
		Sum = (abs(a[i]-b[j])+abs(a[i]-c[k])+abs(b[j]-c[k])) // 2
		MinSum = MinSum if MinSum < Sum else Sum
		MinOFabc = mins(a[i],b[j],c[k])         #找到a[i,b[j],c[k]的最小值
		# 判断哪个是最小值，做出相应的索引移动
		if MinOFabc == a[i]:
			i += 1
			if i >= len(a):
				break
		if MinOFabc == b[j]:
			j += 1
			if j >= len(b):
				break
		if MinOFabc == c[k]:
			k += 1
			if k >= len(c):
				break
		cnt += 1
	return MinSum


if __name__ == "__main__":
	a = [3,4,5,7,15]
	b = [10,12,14,16,17]
	c = [20,21,23,24,37,30]
	print("最小距离为：",MinDistance1(a,b,c))
	print("最小距离为：",MinDistance2(a,b,c))
	print("最小距离为：",MinDistance3(a,b,c))