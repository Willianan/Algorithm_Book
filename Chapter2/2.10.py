# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/25 22:55
Project:AlgorithmBook
Filename:2.10.py
"""

"""
如何从数组中找出满足a + b = c + d的两个数对
题目描述：给定一个数组，找出数组中是否有两个数对(a,b)和(c，d),使得a+b=c+d，其中，a,b,c和d是不同的元素。
如果有多个答案，打印任意一个即可。
"""

class pair:
	def __init__(self,first,second):
		self.first = None
		self.second = None
		self.first = first
		self.second = second

def findPairs(arr):
	# 键为数对的和，值为数对
	sumPair = dict()
	n = len(arr)
	# 遍历数组中所有可能的数对
	i = 0
	while i < n:
		j = i + 1
		while j < n:
			# 如果这个数对的和在map中没有，则放入map中
			sums = arr[i] + arr[j]
			if sums not in sumPair:
				sumPair[sums] = pair(i,j)
			# map中已经存在与sum相同的数对了，找出来并打印出来
			else:
				# 遍历已经遍历过并存储在map中和为sum的数对
				p = sumPair[sums]
				print("("+str(arr[p.first])+","+str(arr[p.second])+"),("+str(arr[i])+","+str(arr[j])+")")
				return True
			j += 1
		i += 1
	return False

if __name__ == "__main__":
	arr =[3,4,7,10,20,9,8]
	findPairs(arr)