# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/23 18:48
Project:AlgorithmBook
Filename:1.4.py
"""

"""
如何对链表进行重新排序
题目描述：给定链表L0->L1->L2->L3···Ln-1->Ln,把链表重新排序为L0->Ln->Ln-1->L2···。
要求：
	(1)、在原链表的基础上进行排序，即不能申请新的结点；
	(2)、只能修改结点的next域，不能修改数据域。
"""

class LNode:
	def __init__(self):
		self.data = None
		self.next = None

'''
*** 方法功能：找出链表head的中间结点，把链表从中间断成两个子链表
*** 输入参数：head：链表头结点
*** 返回值：  链表中间结点
'''
def FindMiddleNode(head):
	if head is None or head.next is None:
		return head
	fast = head                                 # 遍历链表的时候每次向前走两步
	slow = head                                 # 遍历链表的时候每次向前走一步
	slowPre = head                              # 当fast到链表尾时，slow恰好指向链表的中间结点
	while fast is not None and fast.next is not None:
		slowPre = slow
		slow = slow.next
		fast = fast.next.next
	# 把链表断开成两个独立的子链表
	slowPre.next = None
	return slow
'''
*** 方法功能:对不带头结点的单链表翻转
*** 输入参数：head：链表头结点
'''
def Reverse(head):
	if head is None or head.next is None:
		return head
	pre = head                                  # 前驱结点
	cur = head.next                             # 当前结点
	next = cur.next                             # 后继结点
	pre.next = None
	# 使当前遍历到的结点cur指向前驱结点
	while cur is not None:
		next = cur.next
		cur.next = pre
		pre = cur
		cur = cur.next
		cur = next
	return pre

'''
*** 方法功能:对链表进行排序
*** 输入参数：head：链表头结点
'''
def Reorder(head):
	if head is None or head.next is None:
		return
	# 前半部分链表第一个结点
	cur1 = head.next
	mid = FindMiddleNode(head.next)
	# 后半部分链表逆序后的第一个结点
	cur2 = Reverse(mid)
	tmp = None
	# 合并两个链表
	while cur1.next is not None:
		tmp = cur1.next
		cur1.next = cur2
		cur1 = tmp
		tmp = cur2.next
		cur2.next = cur1
		cur2 = tmp
	cur1.next = cur2

if __name__ == "__main__":
	i = 1
	head = LNode()
	head.next = None
	tmp = None
	cur = head
	# 构造第一个链表
	while i < 100:
		tmp = LNode()
		tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		i += 1
	print("排序前：",end='')
	cur = head.next
	while cur is not None:
		print(cur.data,end='->')
		cur = cur.next
	Reorder(head)
	print("\n排序后：",end='')
	cur = head.next
	while cur is not None:
		print(cur.data,end='->')
		cur = cur.next