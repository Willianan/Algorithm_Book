# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/25 11:04
Project:AlgorithmBook
Filename:2.3.py
"""

"""
如何翻转栈的所有元素
题目描述：翻转(颠倒)栈的所有元素
输入：栈{1，2，3，4，5}，其中1处于栈顶
输出：栈{5，4，3，2，1}，其中5处于栈顶
"""

# python中没有栈的模块，建立栈类
class stack:
	# 模拟栈
	def __init__(self):
		self.items = []

	# 判断栈是否为空
	def isEmpty(self):
		return len(self.items) == 0

	# 返回栈的大小
	def size(self):
		return len(self.items)

	# 返回栈顶元素
	def peek(self):
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

'''
*** 方法功能：把栈底元素移动到栈顶
*** 参    数：s：栈的引用   
'''
def moveBottomToTop(s):
	s = stack()
	if s.isEmpty():
		return
	top1 = s.peek()
	s.pop()                              # 弹出栈顶元素
	if not s.isEmpty():
		# 递归不包含栈顶元素的子栈
		moveBottomToTop(s)
		top2 = s.peek()
		s.pop()
		# 交换栈顶元素与子栈栈顶元素
		s.push(top1)
		s.push(top2)
	else:
		s.push(top1)

def reverse_stack(s):
	s = stack()
	if s.isEmpty():
		return
	# 把栈底元素移动到栈顶
	moveBottomToTop(s)
	top = s.peek()
	s.pop()
	# 递归处理子栈
	reverse_stack(s)
	s.push(top)

if __name__ == "__main__":
	s = stack()
	s.push(5)
	s.push(4)
	s.push(3)
	s.push(2)
	s.push(1)
	reverse_stack(s)
	print("\n翻转后出栈顺序为：",end='')
	while not s.isEmpty():
		print(s.peek(),end='')
		s.pop()

"""
如何给栈排序
"""
class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return len(self.items) == 0
	def size(self):
		return len(self.items)
	def peek(self):
		if not self.isEmpty():
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
		self.items.append(item)

'''
*** 方法功能：把栈底元素移动到栈顶
*** 参    数：s：栈的应用
'''
def MoveBottomToTop1(s):
	if s.isEmpty():
		return
	top1 = s.peek()
	s.pop()
	if not s.isEmpty():
		MoveBottomToTop1(s)
		top2 = s.peek()
		if top1 > top2:
			s.pop()
			s.push(top1)
			s.push(top2)
			return
	s.push(top1)

def sortStack(s):
	if s.isEmpty():
		return
	MoveBottomToTop1(s)
	top = s.peek()
	s.pop()
	sortStack(s)
	s.push(top)

if __name__ == "__main__":
	s = Stack()
	s.push(1)
	s.push(3)
	s.push(2)
	s.push(5)
	s.push(4)
	sortStack(s)
	print("\n排序后出栈顺序为：",end='')
	while not s.isEmpty():
		print(s.peek(),end=' ')
		s.pop()