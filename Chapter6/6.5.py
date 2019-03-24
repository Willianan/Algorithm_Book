# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/17 12:15
Project:AlgorithmBook
Filename:6.5.py
"""

"""
如何根据已知随机数生成函数计算新的随机数
题目描述：已知随机数生成函数rand7()能产生的随机数是整数1~7的均匀分布，如何构造rand10()函数，
使其产生的随机数是整数1~10的均匀分布。
"""
import random
# 产生的随机数是整数1~7的均匀分布
def rand7():
	return int(random.uniform(1,7))
# 产生的随机数是整数1~10的均匀分布
def rand10():
	while True:
		x = (rand7()-1)*7 + rand7()
		if x <= 40:
			break
	return x % 10 + 1
if __name__ == "__main__":
	i = 0
	while i != 10:
		print(rand10(),end=' ')
		i += 1