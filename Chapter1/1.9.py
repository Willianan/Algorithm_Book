# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/23 22:16
Project:AlgorithmBook
Filename:1.9.py
"""

"""
如何合并两个有序链表
题目描述：已知两个链表head1和head2各自有序（例如升序排序），请把它们合并成一个链表，要求合并后的链表依然有序。
"""

class LNode:
	def __init__(self):
		self.data = None
		self.next = None

# 方法功能： 构造链表
def ConstructList(start,number):
	i = start
	head = LNode()
	head.next = None
	tmp = None
	cur = head
	while i < number:
		tmp = LNode()
		tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		i += 2
	return head

def PrintList(head):
	cur = head.next
	while cur is not None:
		print(cur.data,end=' ')
		cur = cur.next


'''
*** 方法功能：合并两个升序排列的单链表
*** 输入参数：head1与head2代表两个单链表
*** 返回值：  合并后链表的头结点
'''
def Merge(head1,head2):
	if head1 is None or head1.next is None:
		return head2
	if head2 is None or head2.next is None:
		return head1
	cur1 = head1.next                               # 用来遍历head1
	cur2 = head2.next                               # 用来遍历head2
	head = None                                     # 合并后链表的头结点
	end = None                                      # 合并后链表的尾结点
	# 合并后链表的头结点为第一个结点元素最小的那个链表的头结点
	if cur1.data > cur2.data:
		head = head2
		end = cur2
		cur2 = cur2.next
	else:
		head = head1
		end = cur1
		cur1 = cur1.next
	# 每次找到链表剩余结点的最小值对应的结点连接到合并后链表的尾部
	while cur1 != None and cur2 != None:
		if cur1.data < cur2.data:
			end.next = cur1
			end = cur1
			cur1 = cur1.next
		else:
			end.next = cur2
			end = cur2
			cur2 = cur2.next
	# 当遍历完一个链表后把另外一个链表剩余的结点链接到合并后的链表后面
	if cur1 != None:
		end.next = cur1
	if cur2 != None:
		end.next = cur2
	return head

if __name__ == "__main__":
	head1 = ConstructList(1,10)
	head2 = ConstructList(2,15)
	print("链表head1：",end='')
	PrintList(head1)
	print("\n链表head2： ",end='')
	PrintList(head2)
	print("\n合并后的链表：",end='')
	head = Merge(head1,head2)
	PrintList(head)


