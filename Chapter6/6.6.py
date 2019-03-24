# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/17 12:26
Project:AlgorithmBook
Filename:6.6.py
"""

"""
如何判断1024!末尾有多少0
"""
#方法一：蛮力法
# 方法二：因子法
def zeroCount(n):
	count = 0
	while n > 0:
		n //= 5
		count += n
	return count
if __name__ == "__main__":
	print("1024!末尾0的个数为：",zeroCount(1024))

"""
引申：如何计算N!末尾有几个0？
"""