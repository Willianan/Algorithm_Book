# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/28 15:55
Project:AlgorithmBook
Filename:4.6.py
"""

"""
如何找出数组中第K小的数
题目描述:给定一个整数数组，如何快速地求出该数组中第k小的数。
"""

# 方法一：排序法
# 方法二：部分排序法
# 方法三：类快速排序方法

'''
**** 方法功能：在数组array中找出第k个小的数
**** 输入参数：array：整数数组；low：为数组起始下标；high:数组右边界的下标；k为整数
**** 返回值：  数组中第k小的值  
'''
def findSmallK(array,low,high,k):
	i = low
	j = high
	splitElem = array[i]
	# 把小于等于splitElem的数放到数组中splitElem的左边，大于splitElem的值放到右边
	while i < j:
		while i < j and array[j] >= splitElem:
			j -= 1
		if i < j :
			array[i] = array[j]
			i += 1
		while i < j and array[i] <= splitElem:
			i += 1
		if i < j:
			array[j] = array[i]
	array[i] = splitElem
	# splitElem在子数组array[low~high]中下标的偏移量
	subArrayIndex = i - low
	# splitElem在array[low~high]所在的位置恰好为k-1，那么它就是第k小的值
	if subArrayIndex == k-1:
		return array[i]
	# splitElem在array[low~high]所在的位置大于k-1，那么只需要在array[low~i]中找第k小的值
	elif subArrayIndex > k-1:
		return findSmallK(array,low,i-1,k)
	# 在array[i+1~high]中找第k小的值
	else:
		return findSmallK(array,i+1,high,k-(i-low)-1)
if __name__ == "__main__":
	array = [4,0,1,0,2,3]
	k = 3
	print("第"+str(k)+"小的值为："+str(findSmallK(array,0,len(array)-1,k)))


"""
引申：O(N)时间复杂度内查找数组中前三名
题目描述：在数组中找出前K大的值
"""
def findTop3(array):
	if array == None or len(array) < 3:
		print("参数不合理")
		return
	r1 = r2 = r3 = -2**31
	i = 0
	while i < len(array):
		if array[i] > r1:
			r3 = r2
			r2 = r1
			r1 = array[i]
		elif array[i] > r3 and array[i] != r1:
			r3 = r2
			r2 = array[i]
		elif array[i] > r3 and array[i] != r2:
			r3 = array[3]
		i += 1
	print("前三名分别为："+str(r1)+","+str(r2)+","+str(r3))

if __name__ == "__main__":
	array = [4,7,1,2,3,5,3,6,3,2]
	findTop3(array)