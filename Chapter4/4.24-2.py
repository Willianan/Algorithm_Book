# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/4 10:53
Project:AlgorithmBook
Filename:4.24-2.py
"""

# 方法二：哈希法
def sort(array):
	data_count = dict()
	# 把数组中的数放入map中
	i = 0
	while i < len(array):
		if str(array[i]) in data_count:
			data_count[str(array[i])] = data_count.get(str(array[i])) + 1
		else:
			data_count[str(array[i])] = 1
		i += 1
	index = 0
	for key,value in data_count.items():
		i = value
		while i > 0:
			array[index] = key
			index += 1
			i -= 1
if __name__ == "__main__":
	array = [15,12,15,2,2,12,2,3,12,100,3,3]
	sort(array)
	i = 0
	while i < len(array):
		print(array[i],end=' ')
		i += 1