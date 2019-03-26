# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019/3/20 10:23
@Project:AlgorithmBook
@Filename:8.5.py
"""

"""
如何进行快速排序
"""
def quick_sort(lists,left,right):
	# quick sort
	if left >= right:
		return lists
	key = lists[left]
	low = left
	high = right
	while left < right:
		while left < right and lists[right] >= key:
			right -= 1
		lists[left] = lists[right]
		while left < right and lists[left] <= key:
			left += 1
		lists[right] = lists[left]
	lists[right] = key
	quick_sort(lists,low,left-1)
	quick_sort(lists,left+1,high)
	return lists
if __name__ == "__main__":
	lists = [3,4,2,8,9,5,1,2,7]
	print("排序前的序列为：",end='')
	for i in lists:
		print(i,end=' ')
	print("\n排序后的序列为：",end='')
	for i in quick_sort(lists,0,len(lists)-1):
		print(i,end=' ')
