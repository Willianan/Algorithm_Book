# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/23 20:41
Project:AlgorithmBook
Filename:1.6.py
"""

"""
如何检测一个较大的单链表是否有环
题目描述：单链表有环指的是单链表中某个结点的next域指向的链表中在它之前的某一个结点，这样在链表的尾部形成一个环形
结构。如何判断单链表是否有环存在？
"""
# 方法一：蛮力法
# 方法二：快慢指针遍历法

"""
如果链表纯真环，那么如何找出环的入口点？
"""
class LNode:
	def __init__(self):
		self.data = None
		self.next = None

# 构造链表
def ConstructList():
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
	cur.next = head.next.next.next
	return head

'''
*** 方法功能：判断链表是否有环
*** 输入参数：head:链表头结点
*** 返回值：  None：无环，否则返回slow与fast相遇点的结点
'''
def isLoop(head):
	if head is None or head.next is None:
		return None
	# 初始化slow和fast，都指向链表的第一个结点
	slow = head.next
	fast = head.next
	while fast is not None and fast.next is not None:
		slow =slow.next
		fast = fast.next.next
		if slow == fast:
			return slow

'''
*** 方法功能：找出环的入口点
*** 输入参数：head：fast与slow相遇点
*** 返回值：  None:无环，否则返回slow与fast指针相遇点的结点
'''
def FindLoopNode(head,meetNode):
	first = head.next
	second = meetNode
	while first != second:
		first = first.next
		second = second.next
	return first

if __name__ == "__main__":
	head = ConstructList()
	meetNode = isLoop(head)
	loopNode = None
	if meetNode is not None:
		print("有环")
		loopNode = FindLoopNode(head,meetNode)
		print("环的入口点为：",loopNode.data)
	else:
		print("无环")
