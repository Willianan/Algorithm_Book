# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/17 14:21
Project:AlgorithmBook
Filename:6.11.py
"""

"""
如何找最小的不重复数
题目描述：给定任意一个正整数，求比这个数大且最小的“不重复数”,“不重复数”的含义是相邻两位不相同。
"""
'''
****** 方法功能：处理数字相加的进位
****** 输入参数：num为字符数组；pos为进位加1操作对应的下标位置
'''
def carry(num,pos):
	while pos > 0:
		if int(num[pos]) > 9:
			num[pos] = '0'
			num[pos-1] = str(int(num[pos-1])+1)
		pos -= 1

# 方法一:蛮力法
# 方法二：从右到左的贪心法
'''
****** 功能方法：获取大于n的最小不重复数
****** 输入参数：n为正整数
****** 返回值： 大于n的最小不重复数
'''
def findMinNonDupNum(n):
	count = 0
	nChar = list(str(n+1))
	ch = [None]*(len(nChar)+2)
	ch[0] = '0'
	ch[len(ch)-1] = '0'
	i = 0
	while i < len(nChar):
		ch[i+1] = nChar[i]
		i += 1
	lens = len(ch)
	i = lens - 2
	while i > 0:
		count += 1
		if ch[i-1] == ch[i]:
			ch[i] = str(int(ch[i])+1)                           # 末尾数字加1
			carry(ch,i)                                         # 处理进位
			# 把下标为i后面的字符串变为0101····串
			j = i + 1
			while j < lens:
				if (j-i) % 2 == 1:
					ch[j] = '0'
				else:
					ch[j] = '1'
				j += 1
			# 第i位加1后，可能会与第i+1位相等
			i += 1
		else:
			i -= 1
	print("循环次数为：",count)
	return int(''.join(ch))

if __name__ == "__main__":
	print(findMinNonDupNum(23345))
	print(findMinNonDupNum(1101010))
	print(findMinNonDupNum(99010))
	print(findMinNonDupNum(8989))

# 方法二：从左到右的贪心法
def FindMinNonDupNum(n):
	count = 0
	nchar = list(str(n+1))
	ch = [None]*(len(nchar)+1)
	ch[0] = '0'
	i = 0
	while i < len(nchar):
		ch[i+1] = nchar[i]
		i += 1
	i = 2
	while i < len(ch):
		count += 1
		if ch[i-1] == ch[i]:
			ch[i] = str(int(ch[i])+1)
			carry(ch,i)
			j = i+1
			while j < len(ch):
				if (j-i)%2 == 1:
					ch[j] = '0'
				else:
					ch[j] = '1'
				j += 1
		else:
			i += 1
	print("循环次数为：",count)
	return int(''.join(ch))


if __name__ == "__main__":
	print(FindMinNonDupNum(23345))
	print(FindMinNonDupNum(1101010))
	print(FindMinNonDupNum(99010))
	print(FindMinNonDupNum(8989))