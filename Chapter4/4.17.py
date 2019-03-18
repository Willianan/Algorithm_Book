# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 20:22
Project:AlgorithmBook
Filename:4.17.py
"""

"""
如何寻找最多的覆盖点
题目描述：坐标轴上从左到右依次的点为a[0],a[1],a[2]····a[n-1],设一根木棒的长度为L，求L最多能覆盖坐标轴的几个点。
"""
def maxCover(array,L):
	count = 2
	maxCount = 1                # 最长覆盖的点数
	start = 0                   # 覆盖坐标的起始位置
	i = 0
	j = 1
	while i < len(array) and j < len(array):
		while j < len(array) and array[j] - array[i] <= L:
			j += 1
			count += 1
		j -= 1
		count -=1
		if count > maxCount:
			start = i
			maxCount = count
		i += 1
		j += 1
	print("覆盖的坐标点：",end='')
	i = start
	while i < start+maxCount:
		print(array[i],end=' ')
		i += 1
	print()
	return maxCount

if __name__ == "__main__":
	array = [1,3,7,8,10,11,12,13,15,16,17,19,25]
	print("最长覆盖点数：",maxCover(array,8))