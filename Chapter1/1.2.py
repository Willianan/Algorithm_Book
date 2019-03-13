# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/23 14:58
Project:AlgorithmBook
Filename:1.2.py
"""

'''
如何从无序链表中移除重复项
题目描述：给定一个没有排序的链表，去掉其重复项，并保留原顺序
输入：1->3->1->5->5->7
输出：1->3->5->7
'''
import time
class LNode:
	def __init__(self):
		self.data = None
		self.next = None

# 方法一：顺序删除
'''
** 方法功能：对带头结点的无序单链表删除重复的结点
** 输入参数：head：链表头结点
'''
def removeDup(head):
	if head is None or head.next is None:
		return
	outerCur = head.next                    #用于外层循环，指向链表的第一个结点
	innerCur = None                         #用于内层循环来遍历outerCur后面的 结点
	innerPre = None                         # innerCur的前驱结点
	while outerCur is not None:
		innerCur = outerCur.next
		innerPre = outerCur
		while innerCur is not None:
			# 找到重复的结点并删除
			if outerCur.data == innerCur.data:
				innerPre.next = innerCur.next
				innerCur = innerCur.next
			else:
				innerPre = innerCur
				innerCur = innerCur.next
		outerCur = outerCur.next

# 方法二：递归法
def removeDupRecursion(head):
	if head.next is None:
		return head
	pointer = None
	cur = head
	# 对以head.next为首的子链表删除重复的结点
	head.next = removeDupRecursion(head.next)
	pointer = head.next
	# 找出以head.next为首的子链表中与head结点相同的结点并删除
	while pointer is not None:
		if head.data == pointer.data:
			cur.next = pointer.next
			pointer = cur.next
		else:
			pointer = pointer.next
			cur = cur.next
	return head
"""
*** 方法功能：对带头的结点的单链表删除重复结点
*** 输入参数：head:链表头结点
"""
def removeDuop2(head):
	if head is None:
		return
	head.next = removeDupRecursion(head.next)



if __name__ == "__main__":
	time_start = time.perf_counter()
#	time_start = time.process_time()
	i = 1
	head = LNode()
	tmp = None

	cur = head
	while i < 7:
		tmp = LNode()
		if i % 2 == 0:
			tmp.data = i + 1
		elif i % 3 == 0:
			tmp.data = i - 2
		else:
			tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		i += 1

	print("删除重复结点前：",end='')
	cur = head.next
	while cur is not None:
		print(cur.data,end='->')
		cur = cur.next
	removeDup(head)                 # 方法一测试
#	removeDuop2(head)               # 方法二测试
	print("\n删除重复结点后：",end='')
	cur = head.next
	while cur is not None:
		print(cur.data,end='->')
		cur = cur.next
	time_end = time.perf_counter()
#	time_end = time.process_time()
	print("\n时间：",time_end - time_start)