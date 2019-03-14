# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/25 21:09
Project:AlgorithmBook
Filename:2.6.py
"""

"""
如何用两个栈模拟队列操作
"""

class Stack:
	def __init__(self):
		self.items = []
	def empty(self):
		return len(self.items) == 0
	def size(self):
		return len(self.items)
	def peek(self):
		if not self.empty():
			return self.items[len(self.items) - 1]
		else:
			return None
	def pop(self):
		if not self.empty():
			return self.items.pop()
		else:
			print("The stack was Null!")
			return None
	def push(self,item):
		self.items.append(item)

class MyStack:
	def __init__(self):
		self.A = Stack()                            # 用来存储栈中元素
		self.B = Stack()                            # 用来存储当前栈中最小的元素

	def push(self,data):
		self.A.push(data)
	def pop(self):
		if self.B.empty():
			while not self.A.empty():
				self.B.push(self.A.peek())
				self.A.pop()
		first = self.B.peek()
		self.B.pop()
		return first


if __name__ == "__main__":
	stack = MyStack()
	stack.push(1)
	stack.push(2)
	print("队列首元素为：",stack.pop())
	print("队列首元素为：",stack.pop())