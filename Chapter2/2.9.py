# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/2/25 22:36
Project:AlgorithmBook
Filename:2.9.py
"""

"""
如何从给定的车票中找出旅程
题目描述：给定一趟旅途旅程中所有的车票信息，根据这个车票信息找出这趟旅程的路线。
"""

def printResult(inputs):
	# 用来存储把input的间与值调换后的信息
	reverseInput = dict()
	for k,v in inputs.items():
		reverseInput[v] = k
	start = None
	# 找到起点
	for v,k in inputs.items():
		if k not in reverseInput:
			start = k
			break
	if start == None:
		print("输入不合理")
		return
	# 从起点出发按照顺序遍历路径
	to = inputs[start]
	print(start + "->" + to)
	start = to
	to = inputs[to]
	while to != None:
		print("," + start + "->" + to,end='')
		start = to
		to = inputs[to]

if __name__ == "__main__":
	inputs = dict()
	inputs["西安"] = "成都"
	inputs["北京"] = "上海"
	inputs["大连"] = "西安"
	inputs["上海"] = "大连"
	printResult(inputs)