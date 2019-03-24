# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/17 9:38
Project:AlgorithmBook
Filename:6.2.py
"""

"""
如何判断一个数是否为2的n次方
"""
# 方法一：构造法
def isPower1(n):
	if n < 1:
		return False
	i = 1
	while i <= n:
		if i == n:
			return True
		i <<= 1
	return False


# # 方法二：与操作法
def isPower2(n):
	if n < 1:
		return False
	m = n & (n-1)
	return m == 0
if __name__ == "__main__":
	if isPower2(8):
		print("8能表示成2的n次方")
	else:
		print("8不能表示成2的n次方")
	if isPower1(9):
		print("9能表示成2的n次方")
	else:
		print("9不能表示成2的n次方")