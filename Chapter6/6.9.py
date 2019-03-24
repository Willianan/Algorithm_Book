# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/17 14:06
Project:AlgorithmBook
Filename:6.9.py
"""

"""
如何把十进制数（long型）分别以二进制和十六进制形式输出
"""
def intToBinany(n):
	hexNum = 8 * 8                              # 二进制的位数(long占8个字节)
	bit = []
	for i in range(hexNum):
		b = n >> i
		c,d = divmod(b,2)
		bit.append(str(d))
	return ''.join(bit[::-1])

def intToHex(n):
	hexs = ''
	while n != 0:
		remainder = n % 16
		if remainder < 10:
			hexs = str(remainder+int('\0')) + hexs
		else:
			hexs = str(remainder-10 + ord('A'))+ hexs
		n = n >> 4
	return chr(int(hexs))

if __name__ == "__main__":
	print("10的二进制输出是：",intToBinany(10))
	print("10的十六进制输出为：",intToHex(10))