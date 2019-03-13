# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/24 14:49
Project:AlgorithmBook
Filename:1.11.py
"""

"""
如何判断两个单链表（无环）是否交叉
题目描述：单链表相交指的是两个链表存在完全重合的部分
"""

# 方法一：Hash法
# 方法二：首尾相接法
# 方法三：尾结点法

class LNode:
	def __init__(self):
		self.data = None
		self.next = None

'''
*** 方法功能：判断两个链表是否相交，如果相交找出交点
*** 输入参数：head1和head2分别为两个链表的头结点
*** 返回值： 如果两个链表不相交返回None，如果相交返回相交交点
'''
def IsIntersect(head1,head2):
	if head1 == None or head1.next == None or head2 == None or  head2.next == None:
		return None
	temp1 = head1.next
	temp2 = head2.next
	n1,n2 = 0,0
	# 遍历head1，找到尾结点，同时记录head1的长度
	while temp1.next != None:
		temp1 = temp1.next
		n1 += 1
	# 遍历head2，找出尾结点，同时记录head2的长度
	while temp2.next != None:
		temp2 = temp2.next
		n2 += 1
	# head1与head2是有相同的尾结点
	if temp1 == temp2:
		# 长链表先走|n1-n2|步
		if n1 > n2:
			while n1 -n2 > 0:
				head1 = head1.next
				n1 -= 1
		if n2 > n1:
			while n2 - n1 > 0:
				head2 = head2.next
				n2 -= 1
		# 两个链表同时前进，找出相同的结点
		while head1 != head2:
			head1 = head1.next
			head2 = head2.next
		return head1
	# head1与head2是没有相同的尾结点
	else:
		return None


if __name__ == "__main__":
	i = 1
	# 链表头结点
	head1 =LNode()
	head1.next = None
	# 链表头结点
	head2 = LNode()
	head2.next = None
	tmp = None
	cur = head1
	p = None
	# 构造第1个链表
	while i < 8:
		tmp = LNode()
		tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		if i == 5:
			p = tmp
		i += 1
	cur = head2
	# 构造第2个链表
	i = 1
	while i < 5:
		tmp = LNode()
		tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		i += 1
	# 使它们相交于结点5
	cur.next = p
	interNode = IsIntersect(head1,head2)
	if interNode is None:
		print("这两个链表不相交")
	else:
		print("这两个链表相交点为："+str(interNode.data))