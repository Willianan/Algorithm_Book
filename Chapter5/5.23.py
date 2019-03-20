# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/15 10:05
Project:AlgorithmBook
Filename:5.23.py
"""

"""
如何查找到达目标词最短链长度
题目描述：给定一个词典和两个长度相同的“开始”和“目标”的单词。找到从“开始”到“目标”最小链的长度。
如果它存在，那么这条链中相邻单词只有一个字符不同，而链中的每个单词都是有效的单词，即它存在于字典中。
例如给定一个单词词典：[pooN,pbcc,zamc,poIc,pbca,pbIc,poIN]
start = TooN
target = pbca
输出结果为：7
TooN(start)-- pooN -- PoIN -- poIc -- pbcc -- pbca(target)
"""
from collections import deque
# 用来存储单词链的队列
class QItem:
	def __init__(self,word,lens):
		self.word = word
		self.lens = lens

# 判断两个字符串是否只有一个不相同的字符
def isAdjacent(a,b):
	diff = 0
	i = 0
	while i < len(a):
		if list(a)[i] != list(b)[i]:
			diff += 1
		if diff > 1:
			return False
		i += 1
	return diff == 1

# 返回从start到target的最短链
def shortestChainLen(start,target,D):
	Q = deque()
	item = QItem(start,1)
	Q.append(item)                              # 把第一个字符串添加进来
	while len(Q) > 0:
		curr = Q[0]
		Q.pop()
		for it in D:
			temp = it
			# 如果这两个字符串只有一个字符不同
			if isAdjacent(curr.word,temp):
				item.word = temp
				item.lens = curr.lens + 1
				Q.append(item)                      # 把这个字符串放入队列中
				# 把这个字符串从队列中删除来避免被重复遍历
				D.remove(temp)
				# 通过转变后得到了目标字符
				if temp == target:
					return item.lens
	return 0
if __name__ == "__main__":
	D = []
	D.append("pooN")
	D.append("pbcc")
	D.append("zamc")
	D.append("poIc")
	D.append("pbca")
	D.append("pbIc")
	D.append("poIN")
	start = "TooN"
	target = "pbca"
	print(D)
	print("最短的链的长度为：",shortestChainLen(start,target,D))
