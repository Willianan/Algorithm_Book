# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019/3/20 9:11
@Project:AlgorithmBook
@Filename:7.6.py
"""

"""
如何组合1，2，5这三个数使其和为100
题目描述：求出用1，2，5这三个数不同的个数组合的和为100的组合个数。
"""

# 方法一：蛮力法
def combinationCount1(n):
	count = 0
	num1 = n                    # 1最多的个数
	num2 = n//2                 # 2最多的个数
	num5 = n//5                 # 5最多的个数
	x = 0
	while x <= num1:
		y = 0
		while y <= num2:
			z = 0
			while z <= num5:
				if x+y*2+z*5 == n:
					count += 1
				z += 1
			y += 1
		x += 1
	return count

# 方法二：数字规律法
def combinationCount2(n):
	count = 0
	m = 0
	while m <= n:
		count += (m+2)//2
		m += 5
	return count


if __name__ == "__main__":
	print(combinationCount1(100))
	print(combinationCount2(100))
