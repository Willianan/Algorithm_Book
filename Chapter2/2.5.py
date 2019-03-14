# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/25 20:18
Project:AlgorithmBook
Filename:2.5.py
"""

"""
如何用O(1)的时间复杂度求栈中最小元素
"""

# 模拟栈
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
		if len(self.items) > 0:
			return self.items.pop()
		else:
			print("The stack was Null!")
			return None
	def push(self,item):
		return self.items.append(item)

class MyStack:
	def __init__(self):
		self.elemStack = Stack()                    # 用来存储栈中元素
		self.minStack = Stack()                     # 栈顶永远存储当前elemStack中最小的值
	def push(self,data):
		self.elemStack.push(data)
		# 更新保存最小元素的栈
		if self.minStack.empty():
			self.minStack.push(data)
		else:
			if data < self.minStack.peek():
				self.minStack.push(data)
	def pop(self):
		topData = self.elemStack.peek()
		self.elemStack.pop()
		if topData == self.mins():
			self.minStack.pop()
		return topData
	def mins(self):
		if self.minStack.empty():
			return 2**32
		else:
			return self.minStack.peek()

if __name__ == "__main__":
	stack = MyStack()
	stack.push(5)
	print("栈中最小值为：",stack.mins())
	stack.push(6)
	print("栈中最小值为：",stack.mins())
	stack.push(4)
	print("栈中最小值为：",stack.mins())
	stack.push(1)
	print("栈中最小值为：",stack.mins())
	stack.pop()
	print("栈中最小值为：",stack.mins())
