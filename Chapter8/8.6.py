# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019/3/20 10:49
@Project:AlgorithmBook
@Filename:8.6.py
"""

"""
如何进行希尔排序
"""
def shell_sort(lists):
	"""
	:param lists:
	:return:
	"""
	# shell sort
	step = 2
	group = len(lists) // 2
	while group > 0:
		for i in range(group):
			j = i + group
			while j < len(lists):
				k = j - group
				key = lists[j]
				while k >= 0:
					if lists[k] > key:
						lists[k+group] = lists[k]
						lists[k] = key
					k -= group
				j += group
		group //= step
	return lists

if __name__ == "__main__":
	lists = [3,4,2,1,5,9,0,54,78,21,10]
	print("排序前的序列为：",end='')
	for i in lists:
		print(i,end=' ')
	print("\n排序后的序列为：",end='')
	for i in shell_sort(lists):
		print(i,end=' ')