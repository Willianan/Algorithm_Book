# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019/3/20 11:02
@Project:AlgorithmBook
@Filename:8.7.py
"""

"""
如何进行堆排序
"""
def adjust_heap(lists,i,size):
	lchild = 2 * i + 1
	rchild = 2 * i + 2
	maxs = 1
	if i < size//2:
		if lchild < size and lists[lchild] > lists[maxs]:
			maxs = lchild
		if rchild < size and lists[rchild] > lists[maxs]:
			maxs = rchild
		if maxs != i:
			lists[maxs],lists[i] = lists[i],lists[maxs]
			adjust_heap(lists,maxs,size)

def build_heap(lists,size):
	for i in range(size//2)[::-1]:
		adjust_heap(lists,i,size)

def heap_sort(lists):
	# heap sort
	build_heap(lists,len(lists))
	for i in range(len(lists))[::-1]:
		lists[0],lists[i] = lists[i],lists[0]
		adjust_heap(lists,0,i)
	return lists

if __name__ == "__main__":
	lists = [3,4,2,8,9,6,7,5,1]
	print("排序前的序列为：",end='')
	for i in lists:
		print(i,end=' ')
	print("\n排序后序列为：",end='')
	for i in heap_sort(lists):
		print(i,end=' ')