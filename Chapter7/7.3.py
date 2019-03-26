# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/19 10:45
Project:AlgorithmBook
Filename:7.3.py
"""

"""
如何求正整数n所有可能的整数组合
题目描述：给定一个正整数n，求解出所有和为n的整数组合，要求组合安装递归方式展示，而且唯一。
"""

'''
******* 方法功能：求和为n的所有整数组合
******* 输入参数：sums：正整数；result：存储组合结果；count：记录组合中数字的个数
'''
def getAllCombination(sums,result,count):
	if sums < 0:
		return
	# 数字的组合满足和为sums的条件，打印出所有组合
	if sums == 0:
		print("满足条件的组合：",end='')
		i = 0
		while i < count:
			print(result[i],end=' ')
			i += 1
		print()
		return
	# 打印debug信息，为了方便理解
	print("-------当前组合：",end='')
	i = 0
	while i < count:
		print(str(result[i]),end=' ')
		i += 1
	print("--------------")
	# 确定组合中下一个取值
	i = 1 if count == 0 else result[count-1]
	print("----"+" i = "+str(i)+" count = "+str(count)+"-----")
	while i <= sums:
		result[count] = i
		count += 1
		getAllCombination(sums-i,result,count)              # 求和为sums-i的组合
		count -= 1                                          # 递归完成后，去掉最后一个组合的数字
		i += 1                                              # 找下一个数字最为组合中的数字

# 方法功能：找出和为n的所有整数的组合
def showAllCombination(n):
	if n < 1:
		print("参数不满足要求")
		return
	result = [None]*n                                   # 存储和为n的组合方式
	getAllCombination(n,result,0)


if __name__ == "__main__":
	showAllCombination(4)