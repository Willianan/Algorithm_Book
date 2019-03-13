# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/18 15:57
Project:AlgorithmBook
Filename:1.1.py
"""
"""
如何实现链表的逆序
题目描述：给定一个带头结点的单链表，请将其逆序。
输入：head->1->2->3->4->5->6->7
输出：head->7->6->5->4->3->2->1
"""
class LNode:
    def __init__(self):
        self.data = None  # 数据域
        self.next = None  # 指针域

# 方法功能： 对单链表进行逆序 输入参数： head： 链表头结点
# 方法1： 就地逆序
def Reverse(head):
    # 判断链表是否为空
    if head == None or head.next == None:
        return
    pre = None  # 前驱结点
    cur = None  # 当前结点
    next = None  # 后继结点
    # 把链表首结点变为尾节点
    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
#    cur = cur.next
    cur = next
    # 是当前遍历到的结点cur 指向其前驱结点
    while cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    #  链表的头结点指向倒数第二个结点
    cur.next = pre
    #  链表的头结点指向原来链表的尾结点
    head.next = cur

#方法2：递归法
"""
方法功能：对不带头结点的单链表进行逆序
输入参数：firstRef:链表头结点
"""
def RecursiveReverse(head):
	#如果链表为空或链表中只有一个元素
	if head is None or head.next is None:
		return head
	else:
		#反转后面的结点
		newhead = RecursiveReverse(head.next)
		#把当前遍历的结点加到后面结点逆序后链表的尾部
		head.next.next = head
		head.next = None
	return newhead
"""
方法功能：对带头结点的单链表进行逆序
输入参数：head：链表头结点
"""

def Reverse1(head):
	if head is None:
		return
	# 获取链表第一个结点
	firstNode = head.next
	# 对链表进行逆序
	newhead = RecursiveReverse(firstNode)
	# 头结点指向逆序后链表的第一个结点
	head.next = newhead
	return newhead

#方法3：插入法
def Reverse2(head):
	 # 判断链表是否为空
	 if head is None or head.next is None:
		 return
	 cur = None                             #当前结点
	 next = None                            #后继结点
	 cur = head.next.next
	 # 设置链表的第一个结点为尾结点
	 head.next.next = None
	 # 把遍历到结点插入到头结点的后面
	 while cur is not None:
		 next = cur.next
		 cur.next = head.next
		 head.next = cur
		 cur = next


if __name__ == '__main__':
	i = 1
	# 链表头结点
	head = LNode()
	head.next = None
	tmp = None
	cur = head
	# 构造单链表
	while i < 8:
		tmp = LNode()
		tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		i += 1
	print('逆序前：',end='')
	cur = head.next
	while cur != None:
		print(cur.data,end='->')
		cur = cur.next

	print('\n就地逆序后 Reverse ：',end='')
	Reverse(head)
	cur = head.next
	while cur != None:
		print(cur.data,end='->')
		cur = cur.next

	print('\n递归法逆序后 Reverse1 ：',end='')
	Reverse1(head)
	cur = head.next
	while cur != None:
		print(cur.data,end='->')
		cur = cur.next

	print('\n递归法逆序后 Reverse2 ：',end='')
	Reverse2(head)
	cur = head.next
	while cur != None:
		print(cur.data,end='->')
		cur = cur.next