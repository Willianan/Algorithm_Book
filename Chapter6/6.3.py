# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/17 10:01
Project:AlgorithmBook
Filename:6.3.py
"""

"""
如何不使用除法操作符实现两个正整数的除法
"""
# 方法一：减法
def divide(m,n):
	print(str(m)+"除以"+str(n),end=':')
	res = 0
	remain = m
	# 被除数减除数，直到相减结果小于除数为止
	while m > n:
		m -= n
		res += 1
	remain = m
	print("商为："+str(res)+",余数："+str(remain))

# 方法二：移位法
def divide2(m,n):
	print(str(m)+"除以"+str(n)+":")
	result = 0
	while m >= n:
		multi = 1
		while multi * n <= (m >> 1):
			multi <<= 1
		result += multi
		# 相减结果进入下一次循环
		m -= multi * n
	print("商为："+str(result)+",余数："+str(m))
if __name__ == "__main__":
	m = 14
	n = 4
	divide(m,n)
	divide2(m,n)


"""
引申一：如何不使用加减乘除运算实现加法
"""
def add(n1,n2):
	sums = 0                                # 保存不进位相加结果
	carry = 0                               # 保存进位值
	while True:                             # 判断进位值是否为0
		sums = n1 ^ n2                      # 异或代替不进位相加
		carry = (n1 & n2) << 1              # 与操作代替计算进位值
		n1 = sums
		n2 = carry
		if carry == 0:
			break
	return sums
if __name__ == "__main__":
	print(add(2,4))

"""
引申二：如何不使用加减乘除运算实现减法
"""
def add(n1,n2):
	sums = 0                                # 保存不进位相加结果
	carry = 0                               # 保存进位值
	while True:                             # 判断进位值是否为0
		sums = n1 ^ n2                      # 异或代替不进位相加
		carry = (n1 & n2) << 1              # 与操作代替计算进位值
		n1 = sums
		n2 = carry
		if carry == 0:
			break
	return sums

def sub(a,b):
	return add(a,add(~b,1))


"""
引申三：如何不使用加减乘除运算实现乘法
"""
def add(n1,n2):
	sums = 0                                # 保存不进位相加结果
	carry = 0                               # 保存进位值
	while True:                             # 判断进位值是否为0
		sums = n1 ^ n2                      # 异或代替不进位相加
		carry = (n1 & n2) << 1              # 与操作代替计算进位值
		n1 = sums
		n2 = carry
		if carry == 0:
			break
	return sums

def multi(a,b):
	neg = (a > 0) ^ (b > 0)                     # 结果的正负数标记
	# 首先计算两个正数相乘的结果，最后根据neg确定结果的正负
	if b < 0:
		b = add(~b,1)                           # -b
	if a < 0:
		a = add(~a,1)                           # -a
	return = 0
	# key:1向左移位后的值，value:移位的次数即位置编号
	bit_position = dict()
	# 计算出1向左移位的值
	i = 0
	while i < 32:
		bit_position[i << i] = i
	while b > 0:
		position = bit_position[b & ~(b-1)]
		result += (a << position)
		b &= b-1                                    # 去掉最后一位1
	if neg:
		result = add(~result,1)
	return result


