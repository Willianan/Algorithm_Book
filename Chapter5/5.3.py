# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/6 9:29
Project:AlgorithmBook
Filename:5.3.py
"""

"""
如何对字符串进行反转
题目描述：实现字符串的反转，要求不使用任何系统方法，且时间复杂度最小。
"""
# 方法一:临时变量法
def reverse1(str):
	ch = list(str)
	lens = len(ch)
	i = 0
	j = lens - 1
	while i < j:
		tmp = ch[i]
		ch[i] = ch[j]
		ch[j] = tmp
		i += 1
		j -= 1
	return ''.join(ch)

# 方法二：直接交换法
def reserse2(str):
	ch = list(str)
	lens = len(ch)
	i = 0
	j = lens - 1
	while i < j:
		# python中不能直接对字符串进行异或操作，所以借助ord和chr函数
		ch[i] = chr(ord(ch[i])^ord(ch[j]))
		ch[j] = chr(ord(ch[i])^ord(ch[j]))
		ch[i] = chr(ord(ch[i])^ord(ch[j]))
		i += 1
		j -= 1
	return ''.join(ch)


if __name__ == "__main__":
	str = "abcddefg"
	print("字符串"+str+"翻转后为：")
	print(reverse1(str))
	print(reserse2(str))

"""
引申：如何实现单词翻转
"""

'''
***** 方法功能：实现字符串反转
***** 输入参数：ch:字符数组；front与end：待交换子字符串的首尾下界
'''
def reverseStr(ch,front,end):
	while front < end:
		ch[front] = chr(ord(ch[front])^ord(ch[end]))
		ch[end] = chr(ord(ch[front]) ^ ord(ch[end]))
		ch[front] = chr(ord(ch[front]) ^ ord(ch[end]))
		front += 1
		end -= 1
# 翻转字符串中的单词
def swapWords(str):
	# 对整个字符串进行字符反转操作
	lens = len(str)
	ch = list(str)
	reverseStr(ch,0,lens-1)
	begin = 0
	# 对每个单词进行字符反转操作
	i = 1
	while i < lens:
		if ch[i] == ' ':
			reverseStr(ch,begin,i-1)
			begin = i + 1
		i += 1
	reverseStr(ch,begin,lens-1)
	return ''.join(ch)

if __name__ == "__main__":
	str = "how are you"
	print("字符串"+str+"翻转后为：")
	print(swapWords(str))
