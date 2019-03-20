# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/5 9:30
Project:AlgorithmBook
Filename:5.1.py
"""

"""
如何求一个字符串的所有排列
题目描述：设计一个程序，当输入一个字符串时，要求输出这个字符串的所有排列。
"""

# 方法一：递归法
def swap(str,i,j):
	tmp = str[i]
	str[i] = str[j]
	str[j] = tmp

'''
***** 方法功能：对字符串中的字符进行全排列
***** 输入参数：str：待排列的字符串；start：待排列的子字符串的首字符下标
'''
def Permutation(str,start):
	if str == None or start < 0:
		return
	# 完成全排列后输出当前排列的字符串
	if start == len(str)-1:
		print("".join(str),end=' ')
	else:
		i = start
		while i < len(str):
			# 交换start与i所在位置的字符
			swap(str,start,i)
			#固定第一个字符，对剩余的字符进行全排列
			Permutation(str,start+1)
			# 换原start与i所在位置的字符
			swap(str,start,i)
			i += 1

def Permutation_transe(s):
	str = list(s)
	Permutation(str,0)

# 方法二：非递归法
'''
***** 方法功能：根据当前字符串的组合
***** 输入参数：str:字符数组
***** 返回值：  还有下一个返回True，否则返回False
'''
def getNextPermutation(str):
	end = len(str) - 1                  # 字符串最后一个字符的下标
	cur = end                           # 用来从后向前遍历字符串
	suc = 0                             # cur的后继
	tmp = 0
	while cur != 0:
		# 从后向前开始遍历字符串
		suc = cur
		cur -= 1
		if str[cur] < str[suc]:
			# 相邻递增字符，cur指向较小的字符
			# 找出cur后面最小的字符tmp
			tmp = end
			while str[tmp] < str[cur]:
				tmp -= 1
			# 交换cur和tmp
			swap(str,cur,tmp)
			# 把cur后面的字符串进行翻转
			Reverse(str,suc,end)
			return True
	return False
'''
***** 方法功能：翻转字符串
***** 输入参数：begin和end分别为字符串中的第一个字符和最后一个字符的下标
'''
def Reverse(str,begin,end):
	i = begin
	j = end
	while i < j:
		swap(str,i,j)
		i += 1
		j -= 1
'''
***** 方法功能：获取字符串中字符的所有组合
***** 输入参数：str：字符数组
'''
def Permutation2(s):
	if s == None or len(s) < 1:
		return
	str = list(s)
	str.sort()                          # 升序排列字符串数组
	print(str)
	print("".join(str))
	while getNextPermutation(str):
		print("".join(str),end=' ')



if __name__ == "__main__":
	a = "abc"
	Permutation_transe(a)
	print()
	Permutation2(a)