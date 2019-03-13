# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/23 21:18
Project:AlgorithmBook
Filename:1.7.py
"""

"""
如何把链表相邻元素翻转
题目描述：把链表相邻元素翻转
例如：给定链表为：1->2->3->4->5->6->7,那么翻转后的链表为：2->1->4->3->6->5->7
"""

# 方法一：交换值法

#方法二：就地逆序

class LNode:
	def __init__(self):
		self.data = None
		self.next = None

# 将链表相邻元素翻转
def reverse(head):
	# 判断链表是否为空
	if head is None or head.next is None:
		return
	cur = head.next                                 # 当前遍历结点
	pre = head                                      # 当前结点的前驱结点
	next = None                                     # 当前结点后继节点的后继结点
	while cur != None and cur.next != None:
		next = cur.next.next
		pre.next = cur.next
		cur.next.next = cur
		cur.next = next
		pre = cur
		cur = next

if __name__ == "__main__":
	i = 1
	head = LNode()
	head.next = None
	tmp = None
	cur = head
	while i < 10:
		tmp = LNode()
		tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		i += 1
	print("顺序输出：",end='')
	cur = head.next
	while cur is not None:
		print(cur.data,end=' ')
		cur = cur.next
	reverse(head)
	print("\n相邻元素翻转输出：",end='')
	cur = head.next
	while cur is not None:
		print(cur.data,end=' ')
		cur = cur.next
