# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019/3/20 8:49
@Project:AlgorithmBook
@Filename:7.5.py
"""

"""
如何等概率地从大小为n的数组中选取m个整数
题目描述：随机地从大小为n的数组中选取m个整数，要求每个元素被选中的概率相等。
"""
import random
def getRandomM(array,n,m):
	if array == None or n<= 0 or n < m:
		print("参数不合理")
		return
	i = 0
	while i < m:
		j = random.randint(i,n-1)            # 获取i到n-1间的随机数
		# 随机选出的元素放到数组的前面
		tmp = array[i]
		array[i] = array[j]
		array[j] = tmp
		i += 1


if __name__ == "__main__":
	array = [1,2,3,4,5,6,7,8,9,10]
	n = 10
	m = 6
	getRandomM(array,n,m)
	i = 0
	while i < m:
		print(array[i],end=' ')
		i += 1