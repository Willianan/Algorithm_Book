# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/19 9:52
Project:AlgorithmBook
Filename:7.1.py
"""

"""
如何求数字的组合
题目描述：用1、2、2、3、4、5这六个数字，写一个main函数，打印出所有不同的排列。
要求“4”不能在第三位，“3”与“5”不能连接
"""
class Test:
	def __init__(self,array):
		self.numbers = array
		# 用来标记图中结点是否被遍历过
		self.Visited = [None]*len(self.numbers)
		# 图的二维数组表示
		self.graph = [([None]*len(self.numbers)) for i in range(len(self.numbers))]
		self.n = 6
		# 用来标记图中结点是否被遍历过
		self.Visited = None
		# 数字的组合
		self.combination = ''
		# 存放所有的组合
		self.s = set()
	'''
	****** 功能方法：对图从节点start位置开始进行深度遍历
	****** 输入参数：start：遍历的起始位置
	'''
	def depthFirstSearch(self,start):
		self.Visited[start] = True
		self.combination += str(self.numbers[start])
		if len(self.combination) == self.n:
			# 4不出现在第三个位置
			if self.combination.index("4") != 2:
				self.s.add((self.combination))
		j = 0
		while j < self.n:
			if self.graph[start][j] == 1 and self.Visited[j] == False:
				self.depthFirstSearch(j)
			j += 1
		self.combination = self.combination[:-1]
		self.Visited[start] = False
	'''
	****** 功能方法：获取1、2、2、3、4、5的左右组合，使得“4”不能在第三位，“3”与“5”不能连接
	'''
	def getAllCombinations(self):
		# 构造图
		i = 0
		while i < self.n:
			j = 0
			while j < self.n:
				if i == j:
					self.graph[i][j] = 0
				else:
					self.graph[i][j] = 1
				j += 1
			i += 1
		# 确保在遍历的时候3与5是不可达的
		self.graph[3][5] = 0
		self.graph[5][3] = 0
		# 分别从不同的结点出发深度遍历图
		i = 0
		while i < self.n:
			self.depthFirstSearch(i)
			i += 1

	def PrintAllCombination(self):
		for strs in self.s:
			print(strs)



if __name__ == "__main__":
	array = [1,2,2,3,4,5]
	t = Test(array)
	t.getAllCombinations()
	# 打印所有组合
	t.PrintAllCombination()