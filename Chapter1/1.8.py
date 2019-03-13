# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/23 21:43
Project:AlgorithmBook
Filename:1.8.py
"""

"""
如何把链表以k个结点为一组进行翻转
题目描述：k链表翻转就是指把每k个相邻的结点看成一组进行翻转，如果剩余结点不足k个，则保持不变。
例如：给定链表为：1->2->3->4->5->6->7和一个数K，如果K的值为2，那么翻转后的链表为2->1->4->3->6->5->7,
如果K值为3，那么翻转后链表为：3->2->1->6->5->4->7
"""
class LNode:
	def __init__(self):
		self.data = None
		self.next = None

# 对不带头结点的单链表翻转
def Reverse(head):
	if head == None or head.next == None:
		return
	pre = head                              # 前驱结点
	cur = head.next                         # 当前结点
	next = cur.next                         # 后继结点
	pre.next = None
	# 使当前遍历到的结点cur指向前驱结点
	while cur != None:
		next = cur.next
		cur.next = pre
		pre = cur
		cur = cur.next
		cur = next
	return pre

# 对链表K翻转
def ReverseK(head,k):
	if head == None or head.next == None or k < 2:
		return
	i = 1
	pre = head
	begin = head.next
	end = None
	pNext = None
	while begin != None:
		end = begin
		# 找到从begin开始第K个结点
		while i < k:
			if end.next != None:
				end = end.next
			else:                       #剩余结点的个数小于K
				return
			i += 1
		pNext = end.next
		end.next = None
		pre.next = Reverse(begin)
		begin.next = pNext
		pre = begin
		begin = pNext
		i = 1


if __name__ == "__main__":
	i = 1
	head = LNode()
	head.next = None
	tmp = None
	cur = head
	while i < 8:
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
	ReverseK(head,3)
	print("\nK翻转后输出：",end='')
	cur = head.next
	while cur is not None:
		print(cur.data,end=' ')
		cur = cur.next
	cur = head.next
	while cur is not None:
		tmp = cur
		cur = cur.next