# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/12 10:59
Project:AlgorithmBook
Filename:5.15.py
"""

"""
如何求最长递增子序列的长度
题目描述：假设L=<a1,a2,···,an>是n个不同的实数的序列，L的递增子序列是这样的一个子序列Lin=<ak1,ak2,···,akm>，
其中，k1<k2<···<km且ak1<ak2<···<akm。求最大的m值。
"""

# 方法一：最长公共子串法
# 方法二：动态规划法
def getMaxAscendingLen(strs):
	maxLen = [None]*len(strs)
	maxLen[0] = 1
	maxAscendingLen = 1
	i = 1
	while i < len(strs):
		maxLen[i] = 1
		j = 0
		while j < i:
			if list(strs)[j] < list(strs)[i] and maxLen[j] > maxLen[i]-1:
				maxLen[i] = maxLen[j] + 1
				maxAscendingLen = maxLen[i]
			j += 1
		i += 1
	return maxAscendingLen

if __name__ == "__main__":
	s = "xbcdza"
	print("最长递增子序列的长度为：",getMaxAscendingLen(s))
