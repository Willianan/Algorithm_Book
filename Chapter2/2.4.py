# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/25 15:20
Project:AlgorithmBook
Filename:2.4.py
"""

"""
如何根据入栈序列判断可能的出栈序列
题目描述：输入两个整数序列，其中一个序列表示入栈序列，判断另一个序列有没有可能是
对应的出栈序列
"""

class Stack:
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
			print("The stack was Null!")
			return None
	# 压栈
	def push(self,item):
		self.items.append(item)

def isPopSerical(push,pop):
	if push is None or pop is None:
		return False
	pushLength = len(push)
	popLength = len(pop)
	if pushLength != popLength:
		return False
	pushIndex = 0
	popIndex = 0
	stack = Stack()
	while pushIndex < pushLength:
		# 把push序列依次入栈，直到栈顶元素定于pop序列的第一元素
		stack.push(push[pushIndex])
		pushIndex += 1
		# 栈顶元素出栈，pop序列移动到下一个元素
		while (not stack.isEmpty()) and stack.peek() == pop[popIndex]:
			stack.pop()
			popIndex += 1
	# 栈为空，且pop序列中元素都被遍历过
	return stack.isEmpty() and popIndex == popLength

if __name__ == "__main__":
	push = "12345"
	pop = "32541"
	if isPopSerical(push,pop):
		print(pop + "是" + push + "的一个pop序列")
	else:
		print(pop + "不是" + push + "的一个pop序列")