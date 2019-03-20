# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/6 10:40
Project:AlgorithmBook
Filename:5.6.py
"""

"""
如何对由大小写字母组成的字符数组排序
题目描述：有一个由大小写字母组成的字符串，请对它进行重新组合，使得其中的所有小写字母排在大写字母的前面，
大写字母或小写字母之间不要求保存原来次序。
"""
def ReverseArray(ch):
	lens = len(ch)
	begin = 0
	end = lens - 1
	while begin < end:
		# 正向遍历找到下一个大写字母
		while ch[begin] >= 'a' and ch[end] <= 'z' and end > begin:
			begin += 1
		# 逆向遍历找到下一个小写字母
		while ch[end] >= 'A' and ch[begin] <= 'Z' and end > begin:
			temp = ch[begin]
			ch[begin] = ch[end]
			ch[end] = temp
			end -= 1


if __name__ == "__main__":
	ch = list("AbcSef")
	ReverseArray(ch)
	i = 0
	while i < len(ch):
		print(ch[i],end=' ')
		i += 1
