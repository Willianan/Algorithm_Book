# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019/3/20 10:12
@Project:AlgorithmBook
@Filename:8.4.py
"""

"""
如何进行归并排序
"""
def merge(left,right):
	i,j = 0,0
	result = []
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result

def merge_sort(lists):
	# merge sort
	if len(lists) <= 1:
		return lists
	left = merge_sort(lists[:len(lists)//2])
	right = merge_sort(lists[len(lists)//2:])
	return merge(left,right)

if __name__ == "__main__":
	lists = [3,4,2,8,9,5,1,2]
	print("排序前的序列为：",end='')
	for i in lists:
		print(i,end=' ')
	print("\n排序后的序列为：",end='')
	for i in merge_sort(lists):
		print(i,end=' ')