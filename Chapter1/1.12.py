# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/24 15:59
Project:AlgorithmBook
Filename:1.12.py
"""

"""
如何展开链接列表
题目描述：给定一个有序链表，其中每个结点也表示一个有序链表，结点包含两个类型的指针：
(1)、指向主链表中下一个结点的指针
(2)、指向此结点头的链表
所有链表都被排序
"""

class Node:
	def __init__(self,data):
		self.data = data
		#self.next = None
		self.right = None
		self.down = None
		#self.head = None

class MergeList:
	def __init__(self):
		self.head = None
	# 用来合并两个有序的链表*
	def merge(self,head_a,head_b):
		# 如果有其中一个链表为空，直接返回另外一个链表
		if head_a == None:
			return head_b
		if head_b == None:
			return head_a
		# 把两个链表头中较小的结点赋值给result
		if head_a.data < head_b.data:
			result = head_a
			result.down = self.merge(head_a.down,head_b)
		else:
			result = head_b
			result.down = self.merge(head_a,head_b.down)
		return result
	# 把链表扁平化处理
	def flatten(self,root):
		if root is None or root.right is None:
			return root
		# 递归处理root.right链表
		root.right = self.flatten(root.right)
		# 把root结点对应的链表与右边的链表合并
		root = self.merge(root,root.right)
		return root
	# 把data插入到链表头
	def insert(self,head_ref,data):
		new_node = Node(data)
		new_node.down = head_ref
		head_ref = new_node
		# 返回新的表头结点
		return head_ref
	def printList(self):
		temp = self.head
		while temp  is not None:
			print(temp.data,end=' ')
			temp = temp.down


if __name__ == "__main__":
	L = MergeList()
	# 构造链表
	L.head = L.insert(L.head,31)
	L.head = L.insert(L.head, 8)
	L.head = L.insert(L.head, 6)
	L.head = L.insert(L.head, 3)
	L.head.right = L.insert(L.head.right, 21)
	L.head.right = L.insert(L.head.right, 11)
	L.head.right.right = L.insert(L.head.right.right, 50)
	L.head.right.right = L.insert(L.head.right.right, 22)
	L.head.right.right = L.insert(L.head.right.right, 15)
	L.head.right.right.right = L.insert(L.head.right.right.right, 55)
	L.head.right.right.right = L.insert(L.head.right.right.right, 40)
	L.head.right.right.right = L.insert(L.head.right.right.right, 39)
	L.head.right.right.right = L.insert(L.head.right.right.right, 30)
	# 扁平化链表
	L.head = L.flatten(L.head)
	L.printList()
