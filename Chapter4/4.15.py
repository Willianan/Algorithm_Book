# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/1 19:44
Project:AlgorithmBook
Filename:4.15.py
"""

"""
如何对数组进行循环移位
题目描述：把一个含有N个元素的数组循环右移K(K是正数)位，要求时间复杂度为O(N),且只允许使用两个附加变量。
"""
# 方法一：蛮力法
def rightShift(array,k):
	if array == None or len(array) < 1:
		print("参数不合理")
		return
	while k != 0:
		tmp = array[len(array)-1]
		i = len(array)-1
		while i > 0:
			array[i] = array[i-1]
			i -= 1
		array[0] = tmp
		k -= 1

if __name__ == "__main__":
	k = 4
	array = [1,2,3,4,5,6,7,8]
	rightShift(array,k)
	i = 0
	while i < len(array):
		print(array[i],end=' ')
		i += 1
	print()

# 方法二：空间换时间法
# 方法三：翻转法

def reverse(array,start,end):
	while start < end:
		tmp = array[start]
		array[start] = array[end]
		array[end] = tmp
		start += 1
		end -= 1
def rightShift3(array,k):
	if array == None or len(array) < 1:
		print("参数不合理")
		return
	k %= len(array)
	reverse(array,0,len(array)-k-1)
	reverse(array,len(array)-k,len(array)-1)
	reverse(array,0,len(array)-1)

if __name__ == "__main__":
	k = 4
	array = [1,2,3,4,5,6,7,8]
	rightShift3(array,k)
	i = 0
	while i < len(array):
		print(array[i],end=' ')
		i += 1

"""
引申：上述问题中k不一定为正整数，又可能为负整数。当k为负整数时，右移k位，可以理解为左移(-k)位
"""