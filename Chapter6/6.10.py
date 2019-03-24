# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/17 14:15
Project:AlgorithmBook
Filename:6.10.py
"""

"""
如何求二进制数中1的个数
题目描述：给定一个整数，输出这个整数的二进制表示中1的个数。
"""

# 方法一：移位法
def countOne(n):
	count = 0
	while n > 0:
		if (n&1) == 1:      # 判断最后一位是否为1
			count += 1
		n >>= 1             # 移位丢掉最后一位
	return count


# 方法二：与操作法
def countOne2(n):
	count = 0
	while n > 0:
		if n != 0:
			n &= n-1
		count += 1
	return count

if __name__ == "__main__":
	print(countOne(7))
	print(countOne2(8))
