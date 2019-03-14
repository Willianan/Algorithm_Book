# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/24 16:37
Project:AlgorithmBook
Filename:2.1.py
"""

"""
如何实现栈
题目描述：实现一个栈的数据结构，使其具有以下方法：压栈、弹栈、取栈顶元素、判断栈是否为日空以及获取栈中元素个数
"""
# 方法一：数组实现
class MyStack1:
	def __init__(self):
		self.items = []
	# 判断栈是否为空
	def isEmpty(self):
		return len(self.items) == 0
	# 返回栈的大小
	def size(self):
		return len(self.items)
	# 返回栈顶元素
	def top(self):
		if not self.isEmpty():
			return self.items[len(self.items) - 1]
		else:
			return None
	# 弹栈
	def pop(self):
		if len(self.items) > 0:
			return self.items.pop()
		else:
			print("栈已经为空")
			return None
	# 压栈
	def push(self,item):
		self.items.append(item)

if __name__ == "__main__":
	s = MyStack1()
	s.push(4)
	print("栈顶元素为：" + str(s.pop()))
	print("栈大小为：" + str(s.size()))
	s.pop()
	print("弹栈成功")
	s.pop()

# 方法二：链表实现
class LNode:
	def __new__(cls, x):
		cls.data = x
		cls.next = None

class MyStack2:
	def __init__(self):
		self.data = None
		self.next = None

	# 判断stack是否为空，如果为空返回true，否则返回false
	def empty(self):
		if self.next == None:
			return True
		else:
			return False
	# 获取栈中元素的个数
	def size(self):
		size = 0
		p = self.next
		while p != None:
			p = p.next
			size += 1
		return size
	# 入栈：把e放到栈顶
	def push(self,e):
		p = LNode
		p.data = e
		p.next = self.next
		self.next = p
	# 出栈，同时返回栈顶元素
	def pop(self):
		tmp = self.next
		if tmp != None:
			self.next = tmp.next
			return tmp.data
		print("栈已经为空")
		return None
	# 取得栈顶元素
	def top(self):
		if self.next != None:
			return self.next.data
		print("栈已经为空")
		return None


if __name__ == "__main__":
	stack = MyStack2()
	stack.push(1)
	print("栈顶元素为："+ str(stack.top()))
	print("栈的大小为：" + str(stack.size()))
	stack.pop()
	print("弹栈成功")
	stack.pop()
