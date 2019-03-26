# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019/3/20 11:13
@Project:AlgorithmBook
@Filename:8.8.py
"""

"""
如何进行基数排序
"""
import math

def radix_sort(lists,radix=10):
	"""
	:param lists:
	:param radix:
	:return:
	"""
	k = int(math.ceil(math.log(max(lists),radix)))
	bucket = [[] for i in range(radix)]
	for i in range(1,k+1):
		for j in lists:
			bucket[j//(radix ** (i-1))%(radix ** i)].append(j)
		del lists[:]
		for z in bucket:
			lists += z
			del z[:]
	return lists

if __name__ == "__main__":
	lists = [3,4,2,8,9,5,1]
	print("排序前的序列为：",end='')
	for i in lists:
		print(i,end=' ')
	print("\n排序后的序列为：",end='')
	for i in radix_sort(lists):
		print(i,end=' ')