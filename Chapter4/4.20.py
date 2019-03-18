# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 21:50
Project:AlgorithmBook
Filename:4.20.py
"""

"""
如何获取最好的矩阵链相乘方法
题目描述：给定一个矩阵序列，找到最有效的方式将这些矩阵相乘在一起。给定表示矩阵链的数组p,使得
"""
# 方法一：递归法
def MatrixChainOrder1(p,i,j):
	if i == j:
		return 0
	mins = 2**32
	# '''
	# 通过把括号放在第一个不同的地方来获取最小的代价
	# 每个括号内可以递归地使用相同的方法来计算
	# '''
	k = i
	while k < j:
		count = MatrixChainOrder1(p,i,k) + MatrixChainOrder1(p,k+1,j) + p[i-1]*p[k]*p[j]
		if count < mins:
			mins = count
		k += 1
	return mins

# 方法二：动态规划
def MatrixChainOrder2(p,n):
	cost =[([None]*n) for i in range(n)]
	i = 1
	while i < n:
		cost[i][i] = 0
		i += 1
	cLen = 2
	while cLen < n:
		i = 1
		while i < n-cLen+1:
			j = i+cLen-1
			cost[i][j] = 2**31
			k = i
			while k <=j-1:
				q = cost[i][k]+cost[k+1][j]+p[i-1]*p[k]*p[j]
				if q < cost[i][j]:
					cost[i][j] = q
				k += 1
			i += 1
		cLen += 1
	return cost[1][n-1]
if __name__ == "__main__":
	array = [1,5,2,4,6]
	print("最少的乘法次数为：",MatrixChainOrder1(array,1,len(array)-1))
	print("最少的乘法次数为：",MatrixChainOrder2(array,len(array)))
