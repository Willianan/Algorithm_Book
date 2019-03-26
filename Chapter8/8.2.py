# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019/3/20 9:58
@Project:AlgorithmBook
@Filename:8.2.py
"""

"""
如何进行插入排序
"""
def insert_sort(lists):
	# insert sort
	for i in range(1,len(lists)):
		key = lists[i]
		j = i - 1
		while j >= 0:
			if lists[j] > key:
				lists[j+1] = lists[j]
				lists[j] = key
			j -= 1
	return lists

if __name__ == "__main__":
	lists = [3,4,2,8,9,5,1,]
	print("排序前的序列为：",end='')
	for i in lists:
		print(i,end=' ')
	print("\n排序后的序列为；",end='')
	for i in insert_sort(lists):
		print(i,end=' ')