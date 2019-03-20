# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/11 10:51
Project:AlgorithmBook
Filename:5.9-2.py
"""

# 方法二：KMP算法
'''
***** 方法功能：求字符串的next数组
***** 输入参数：p为字符串，next为p的next数组
'''
def getNext(p,next):
	i = 0
	j = -1
	next[0] = -1
	while i < len(p):
		if j == -1 or list(p)[i] == list(p)[j]:
			i += 1
			j += 1
			next[i] = j
		else:
			j = next[j]

def	match(s,p,nexts):
	# 检查参数的合理性，s的长度不一定会小于p的长度
	if s == None or p == None:
		print("参数不合理")
		return -1
	slength = len(s)
	plength = len(p)
	# p肯定不是s的子串
	if slength < plength:
		return -1
	i = 0
	j = 0
	while i < slength and j < plength:
		print("i = "+str(i)+",j = "+str(j))
		if j == -1 or list(s)[i] == list(p)[j]:
			# 如果相同，那么继续比较后面的字符
			i += 1
			j += 1
		else:
			# 主串不需要回溯，从next数组中找出需要比较的模式串的位置j
			j = nexts[j]
	if j > plength:
		return i - plength
	return -1

if __name__ == "__main__":
	s = "abababaabcbab"
	p = "abaabc"
	lens = len(p)
	nexts = [0]*(lens+1)
	getNext(p,nexts)
	print("next数组为：",str(nexts[0]),end='')
	i = 1
	while i < lens-1:
		print(","+str(nexts[i]),end='')
		i += 1
	print()
	print("匹配结果为："+str(match(s,p,nexts)))