# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019/3/20 9:47
@Project:AlgorithmBook
@Filename:8.1.py
"""

"""
如何进行选择排序
"""
def select_sort(lists):
	# select sort
	for i in range(len(lists)):
		min = i
		for j in range(i+1,len(lists)):
			if lists[min] > lists[j]:
				min = j
		lists[min],lists[i] = lists[i],lists[min]
	return lists

if __name__ == "__main__":
	lists = [3,4,2,8,9,5,1,12,54,38,27,11]
	print("排序前序列为：",end='')
	for i in lists:
		print(i,end=' ')
	print("\n排序后的结果为：",end='')
	for i in select_sort(lists):
		print(i,end=' ')