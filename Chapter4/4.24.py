# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/4 10:14
Project:AlgorithmBook
Filename:4.24.py
"""

"""
如何对大量重复的数字的数组排序
题目描述：给定一个数组，已知这个数组中有大量的重复的数字，如何对这个数组进行高效地排序
"""

# 方法一：AVL树

# AVL树的结点
class AVLNode:
	def __init__(self,data):
		self.data = data
		self.left = self.right = None
		self.height = self.count = 1

class Sort:
	# 中序遍历AVL树，把遍历结果放入到数组中
	def inorder(self,array,root,index):
		if root != None:
			# 中序遍历左子树
			index = self.inorder(array,root.left,index)
			# 把root结点对应的数字根据出现的次数放入到数组中
			i = 0
			while i < root.count:
				array[index] = root.data
				index += 1
				i += 1
			# 中序遍历右子树
			index = self.inorder(array,root.right,index)
		return index
	# 得到树的高度
	def getHeight(self,node):
		if node == None:
			return 0
		else:
			return node.height
	# 把以y为根的子树向右旋转
	def rightRotate(self,y):
		x = y.left
		T2 = x.right
		# 旋转
		x.right = y
		y.left = T2
		y.height = max(self.getHeight(y.left),self.getHeight(y.right)) + 1
		x.height = max(self.getHeight(x.left),self.getHeight(x.right)) + 1
		# 返回新的根节点
		return x
		# 把以x为根的子树向右旋转
	def leftRotate(self,x):
		y = x.right
		T2 = y.left
		y.left = x
		x.right = T2
		x.height = max(self.getHeight(x.left),self.getHeight(x.right)) + 1
		y.height = max(self.getHeight(y.left),self.getHeight(y.right)) + 1
		return y
	# 获取树的平衡因子
	def getBalance(self,N):
		if N == None:
			return 0
		return self.getHeight(N.left) - self.getHeight(N.right)
	# '''
	# 如果data在AVL树中不存在，则把data插入到AVL树中，
	# 否则把这个节点对应的count加1
	# '''
	def insert(self,root,data):
		if root == None:
			return AVLNode(data)
		# data在树中存在，把对应的结点的count加1
		if data == root.data:
			root.count += 1
			return root
		# 在左子树中继续查找data是存在
		if data < root.data:
			root.left = self.insert(root.left,data)
		# 在右子树中继续查找data是否存在
		else:
			root.right = self.insert(root.right,data)
		# 插入新的结点后更新root结点的高度
		root.height = max(self.getHeight(root.left),self.getHeight(root.right)) + 1
		# 获取树的平衡因子
		balance = self.getBalance(root)
		# 如果树不平衡，根据数据结构中学过的四种情况进行调整
		# LL型
		if balance > 1 and data < root.left.data:
			return self.rightRotate(root)
		# RR型
		elif balance < -1 and data > root.right.data:
			return self.leftRotate(root)
		# LR型
		elif balance > 1 and data > root.left.data:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)
		# RL型
		elif balance < -1 and data < root.right.data:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)
		# 返回树的根结点
		return root

	# 使用AVL树实现排序
	def sort(self,array):
		root = None
		i = 0
		while i < len(array):
			root = self.insert(root,array[i])
			i += 1
		index = 0
		self.inorder(array,root,index)

if __name__ == "__main__":
	array = [15,12,15,2,2,12,2,3,12,100,3,3]
	s = Sort()
	s.sort(array)
	i = 0
	while i < len(array):
		print(array[i],end=' ')
		i += 1
