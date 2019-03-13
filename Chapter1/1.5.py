# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/23 19:30
Project:AlgorithmBook
Filename:1.5.py
"""

"""
如何找出单链表中的倒数第K个元素
题目描述：找出链表中倒数第K个元素
例如：给定单链表：1—>2->3->4->5->6->7,则单链表的倒数第k=3个元素是5
"""
# 方法一：顺序遍历两遍法

#方法二：快慢指针法

class LNode:
	def __init__(self):
		self.data = None
		self.next = None

# 构建一个单链表
def ConstructList():
	i = 1
	head = LNode()
	head.next = None
	tmp = None
	cur = head
	# 构造第一个链表
	while i < 8:
		tmp = LNode()
		tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		i += 1
	return head

#顺序打印单链表结点的数据
def PrintList(head):
	cur = head.next
	while cur is not None:
		print(cur.data,end='->')
		cur = cur.next

'''
*** 方法功能：找出链表倒数第k个结点
*** 输入参数：head：链表头结点
*** 返回值： 倒数第k个结点
'''
def FindlastK(head,k):
	if head is None or head.next is None:
		return
	slow = LNode()
	fast = LNode()
	slow = head.next
	fast = head.next
	i = 0
	while i < k and fast is not None:
		fast = fast.next
		i += 1
	if i < k:
		return None
	while fast is not None:
		slow = slow.next
		fast = fast.next
	return slow

if __name__ == "__main__":
	head = ConstructList()                  # 链表头指针
	result = None
	print("链表：",end='')
	PrintList(head)
	result = FindlastK(head,3)
	if result is not None:
		print("\n链表倒数第3个元素为：" + str(result.data))

"""
如何将单链表向右旋转k个位置
题目描述：给定单链表并以第K个位置向右旋转。
例如：给定单链表1->2->3->4->5->6->7,k=3,那么旋转后的单链表为5->6->7->1->2->3->4
"""
class LNode:
	def __init__(self):
		self.data = None
		self.next = None

# 方法功能：把链表右旋k个位置
def RotateK(head,k):
	if head == None or head.next == None:
		return
	# fast指针先走k步，然后与slow指针同时向后走
	slow,fast,tmp = LNode(),LNode(),LNode()
	slow,fast = head.next,head.next
	i = 0
	while i < k and fast != None:               # 前移k步
		fast = fast.next
		i += 1
	# 判断k是否已超出链表长度
	if i < k :
		return
	# 循环结束后slow指向链表倒数第k+1个元素，fast指向链表最后一个元素
	while fast.next != None:
		slow = slow.next
		fast = fast.next
	tmp = slow
	slow = slow.next
	tmp.next = None
	fast.next = head.next
	head.next = slow

def ConstructList():
	i = 1
	head = LNode()
	head.next = None
	tmp = None
	cur = head
	# 构造第一个链表
	while i < 8:
		tmp = LNode()
		tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		i += 1
	return head

# 顺序打印单链表结点的数据
def PrintList(head):
	cur = head.next
	while cur is not None:
		print(cur.data,end=' ')
		cur = cur.next

if __name__ == "__main__":
	head = ConstructList()
	print("旋转前：",end='')
	PrintList(head)
	RotateK(head,3)
	print("\n旋转后：",end='')
	PrintList(head)
