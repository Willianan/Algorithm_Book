# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/25 21:57
Project:AlgorithmBook
Filename:2.8.py
"""

"""
如何实现LRU缓存方案
题目描述：LRU是Least Recently Used的缩写，它的意思是“最近很少使用”，LRU环存就是
使用这种原理实现，简单的说就是缓存一定量的数据，当超过设定的阈值时就把一些过期的数据
删除掉。常用于页面置换算法，时虚拟页式存储管理中常用的算法。
"""

from collections import deque

class LRU:
	def __init__(self,casheSize):
		self.casheSize = casheSize
		self.queue = deque()
		self.hashSet = set()

	# 判断缓存队列是否已满
	def isQueueFull(self):
		return len(self.queue) == self.casheSize
	# 把页号为pageNum的页缓存到队列中，同时添加到Hash表中
	def enQueue(self,pageNum):
		#如果队列已满，需要删除队尾的缓存的页
		if self.isQueueFull():
			self.hashSet.remove(self.queue[-1])
			self.queue.pop()
		self.queue.appendleft(pageNum)
		# 把新缓存的结点同时添加到hash表中
		self.hashSet.add(pageNum)

# '''
# 当访问某一个page的时候，会调用这个函数，对于访问的page有两种情况：
# 	(1)、如果page在缓存队列中，直接把这个结点移动到队首
# 	(2)、如果page不在缓存队列中，把这个page缓存到队首
# '''

	def accessPage(self,pageNum):
		# page不在缓存队列中，把它缓存到队首
		if pageNum not in self.hashSet:
			self.enQueue(pageNum)
		# page已经在缓存队列中，移动到队首
		elif pageNum != self.queue[0]:
			self.queue.remove(pageNum)
			self.queue.appendleft(pageNum)
	def printQueue(self):
		while len(self.queue) > 0:
			print(self.queue.popleft(),end='  ')


if __name__ == "__main__":
	# 假设缓存大小为3
	lru = LRU(3)
	lru.accessPage(1)
	lru.accessPage(2)
	lru.accessPage(5)
	lru.accessPage(1)
	lru.accessPage(16)
	lru.accessPage(17)
	# 通过上面的访问序列后，缓存的信息为
	lru.printQueue()
