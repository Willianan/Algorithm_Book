# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019/3/20 10:05
@Project:AlgorithmBook
@Filename:8.3.py
"""

"""
如何进行冒泡排序
"""
def bubble_sort(lists):
	# bubble sort
	for i in range(len(lists)):
		for j in range(i+1,len(lists)):
			if lists[i] > lists[j]:
				lists[i],lists[j] = lists[j],lists[i]
	return lists

if __name__ == "__main__":
	lists = [3,4,2,8,19,5,7,4,1]
	print("排序前的序列为：",end='')
	for i in lists:
		print(i,end=' ')
	print("\n排序后的序列为：",end='')
	for i in bubble_sort(lists):
		print(i,end=' ')