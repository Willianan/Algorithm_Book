# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/14 10:59
Project:AlgorithmBook
Filename:5.20.py
"""

"""
如何在二维数组中寻找最短路线
题目描述：寻找一条从左上角(arr[0][0])到右下角(arr[m-1][n-1])的路线，使得沿途经过的数组中的整数的和最小。
"""

# 方法一：递归法
def getMinPath(arr,i,j):
	# 倒着走了第一一个结点，递归结束
	if i == 0 and j == 0:
		return arr[i][j]
	# 选取两条可能路径上的最小值
	elif i > 0 and j > 0:
		return arr[i][j]+min(getMinPath(arr,i-1,j),getMinPath(arr,i,j-1))
	# 下面两个条件只可选其一
	elif i > 0 and j == 0:
		return arr[i][j] + getMinPath(arr,i-1,j)
	else:
		return arr[i][j] + getMinPath(arr,i,j-1)

def getMinPath1(arr):
	if arr == None or len(arr) == 0:
		return 0
	return getMinPath(arr,len(arr)-1,len(arr[0])-1)

# 方法二：动态规划法
def getMinPath2(arr):
	if arr == None or len(arr) == 0:
		return 0
	# 用来保存计算的中间值
	cache = [([None]*(len(arr))) for i in range(len(arr[0]))]
	cache[0][0] = arr[0][0]
	i = 1
	while i < len(arr[0]):
		cache[0][i] = cache[0][i-1]+arr[0][i]
		i += 1
	j = 1
	while j < len(arr):
		cache[j][0] = cache[j-1][0] + arr[j][0]
		j += 1
	# 在遍历二维数组的过程中不断把结算结果保存到cache中
	print("路径：")
	i = 1
	while i < len(arr):
		j = 1
		while j < len(arr[0]):
			# 可以确定选择的路线为arr[i][j-1]
			if cache[i-1][j] > cache[i][j-1]:
				cache[i][j] = cache[i][j-1] + arr[i][j]
				print("["+str(i)+","+str(j-1)+"] ",end='')
			# 可以确定选择的路线为a[i-1][j]
			else:
				cache[i][j] = cache[i-1][j]+arr[i][j]
				print("["+str(i-1)+","+str(j)+"] ",end='')
			j += 1
		i += 1
	print("["+str(len(arr)-1)+","+str(len(arr[0])-1)+"]",end='')
	print()
	return "最小值为："+str(cache[len(arr)-1][len(arr[0])-1])


if __name__ == "__main__":
	arr = [[1,4,3],[8,7,5],[2,1,5]]
	print(getMinPath1(arr))
	print(getMinPath2(arr))