# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/12 9:51
Project:AlgorithmBook
Filename:5.12.py
"""

"""
如何判断一个字符串是否包含重复字符
题目描述：判断一个字符串是否包含重复字符
"""

# 方法一：蛮力法
# 判断字符串中是否有相同的字符
def isDup(strs):
	i = 0
	while i < len(strs):
		j = i + 1
		while j < len(strs):
			if list(strs)[j] == list(strs)[i]:
				return True
			j += 1
		i += 1
	return False

# 空间换时间
def isDup2(strs):
	flag = [None]*8                     # 只需要8个32位的int，8*32 = 256位
	i = 0
	while i < len(strs):
		index = ord(list(strs)[i]) // 32
		shift = ord(list(strs)[i]) % 32
		if (flag[index] & (1 << shift)) != 0:
			return True
		flag[index] |= (1 << shift)
	return False

if __name__ == "__main__":
	strs = "Good"
	if isDup(strs):
		print(strs+"中有重复字符")
	else:
		print(strs+"没有重复字符")
	# if isDup2(strs):
	# 	print(strs+"中有重复字符")
	# else:
	# 	print(strs+"没有重复字符")