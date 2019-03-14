# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/25 21:22
Project:AlgorithmBook
Filename:2.7.py
"""

"""
如何设计一个排序系统
题目描述：请设计一个排队系统，能够让每个进入队伍的用户都能看到自己在队列中所处的位置和变化，
队伍可能随时有人加入和退出；当有人退出影响到用户的位置排名时需要及时反馈到用户。
"""

from collections import deque

class User:
	def __init__(self,id,name):
		self.id = id                                # 唯一标识一个用户
		self.name = name
		self.seq = 0
	def getName(self):
		return self.name
	def getSeq(self):
		return self.seq
	def setSeq(self,seq):
		self.seq = seq
	def getId(self):
		return self.id
	# def equals(self,arg0):
	# 	o = arg0
	# 	return self.id = o.getId()
	def toString(self):
		return "id:" + str(self.id) + " name:" + self.name + " seq:" + str(self.seq)

class MyQueue:
	def __init__(self):
		self.deque = deque()
	def enQueue(self,user):                         # 进入队列尾部
		user.setSeq(len(self.deque) + 1)
		self.deque.append(user)
	# 队头出队列
	def deQueue(self):
		self.deque.popleft()
		self.updateSeq()
	# 队列中的人随机离开
	def deQueueMove(self,user):
		self.deque.remove(user)
		self.updateSeq()
	# 出队列后更新队列中每个人的序列
	def updateSeq(self):
		i = 1
		for user in self.deque:
			user.setSeq(i)
			i += 1
	# 打印队列的信息
	def printList(self):
		for user in self.deque:
			print(user.toString())


if __name__ == "__main__":
	user1 = User(1,"user1")
	user2 = User(2, "user2")
	user3 = User(3, "user3")
	user4 = User(4, "user4")
	user5 = User(5, "user5")
	queue = MyQueue()
	queue.enQueue(user1)
	queue.enQueue(user2)
	queue.enQueue(user3)
	queue.enQueue(user4)
	queue.enQueue(user5)
	queue.deQueue()                             # 队列元素user1出列
	queue.deQueueMove(user3)                    # 队列中间的元素user3出队列
	queue.enQueue(user1)
	queue.printList()
