# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/24 14:19
Project:AlgorithmBook
Filename:1.10.py
"""

"""
如何在只给定单链表中某个结点的指针的情况下删除该结点
题目描述:删除单链表的指定结点
例如：链表：1->2->3->4->5->6->7,删除指向第5个元素的结点，删除后的链表为：1->2->3->4->6->7
"""

class LNode:
	def __init__(self):
		self.data = None
		self.next = None


def PrintList(head):
	cur = head.next
	while cur is not None:
		print(cur.data,end=' ')
		cur = cur.next

# def ConstructList(start,number):
# 	i = start
# 	head = LNode()
# 	head.next = None
# 	cur = head
# 	tmp = None
# 	while i < number:
# 		tmp = LNode()
# 		tmp.data = i
# 		tmp.next = None
# 		cur.next = tmp
# 		cur = tmp
# 		i += 3
# 	return head

'''
*** 方法功能：给定链表中某个结点，删除该结点
*** 输入参数：链表中的某个结点
*** 返回值：  true：删除成功；false：删除失败
'''
def RemoveNode(p):
	# 如果结点为空，或结点p无后继节点则无法删除
	if p == None or p.next == None:
		return False
	p.data = p.next.data
	tmp = p.next
	p.next = tmp.next
	return True

if __name__ == "__main__":
	p = None
	i = 1
	head = LNode()
	head.next = None
	tmp = None
	cur =head
	while i < 8:
		tmp = LNode()
		tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		if i == 5:
			p = tmp
		i += 1
	print("删除节点"+str(p.data)+"前链表：",end='')
	PrintList(head)
	result = RemoveNode(p)
	if result:
		print("\n删除该节点后链表：",end='')
		PrintList(head)
