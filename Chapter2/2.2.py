# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/24 19:23
Project:AlgorithmBook
Filename:2.2.py
"""

"""
如何实现队列
题目描述：实现一个队列的数据结构，使其具有入队列、出队列、查看队列首尾元素、查看队列大小等功能。
"""

# 方法一：数组实现
# class MyQueue:
# 	def __init__(self):
# 		self.arr = []
# 		self.front = 0                               # 队列首
# 		self.rear = 0                                # 队列尾
#
# 	# 判断队列是否为空
# 	def isEmpty(self):
# 		return self.front == self.rear
# 	# 返回队列的大小
# 	def size(self):
# 		return self.rear - self.front
# 	# 返回队列首元素
# 	def getFront(self):
# 		if self.isEmpty():
# 			return None
# 		return self.arr[self.front]
# 	# 返回队列尾元素
# 	def getBack(self):
# 		if self.isEmpty():
# 			return None
# 		return self.arr[self.rear - 1]
# 	# 删除队列头元素
# 	def deQueue(self):
# 		if self.rear > self.front:
# 			self.front += 1
# 		else:
# 			print("队列已经为空")
# 	# 把新元素加入队列尾
# 	def enQueue(self,item):
# 		self.arr.append(item)
# 		self.rear += 1
#
# if __name__ == "__main__":
# 	queue = MyQueue()
# 	queue.enQueue(1)
# 	queue.enQueue(2)
# 	queue.enQueue(6)
# 	print("队列头元素为：",queue.getFront())
# 	print("队列尾元素为：",queue.getBack())
# 	print("队列的大小为：",queue.size())

# 方法二：链表实现
class LNode:
	def __init__(self,elem):
		self.data = elem
		self.next = None

class MyQueue1(object):
	def __init__(self):
		self.pHead = None
		self.pEnd = None

	# 判断队列是否为空
	def isEmpty(self):
		return self.pHead is None

	# 获取队列中元素的个数
	def size(self):
		size = 0
		p = self.pHead
		while p is not None:
			p = p.next
			size += 1
		return size

	# 入队列，把元素e加入到队列尾
	def enQueue(self,elem):
		p = LNode(elem)
		if self.isEmpty():
			self.pHead = p
			self.pEnd = p
		else:
			self.pEnd.next = p
			self.pEnd = p

	# 出队列，删除队列首元素
	def deQueueHead(self):
		if self.isEmpty():
			print("出队列失败，队列已经为空")
		self.pHead = self.pHead.next
		if self.pEnd == None:
			self.pEnd = None

	# 取得队列首元素
	def getFront(self):
		if self.isEmpty():
			print("获取队列首元素失败，队列已经为空")
			return None
		return self.pHead.data

	# 获取队列尾元素
	def getrear(self):
		if self.pEnd == None:
			print("获取队列尾元素失败，队列已经为空")
			return None
		return self.pEnd.data





if __name__ == "__main__":
	queue = MyQueue1()
	queue.enQueue(1)
	queue.enQueue(2)
	queue.enQueue(9)
	print("队列头元素为：",queue.getFront())
	print("队列尾元素为：",queue.getrear())
	print("队列的大小为：",queue.size())