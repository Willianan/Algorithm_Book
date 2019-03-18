# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/4 10:14
Project:AlgorithmBook
Filename:4.26.py
"""

"""
如何对磁盘分区
"""

def is_allocable(d,p):
	dIndex = 0               # 磁盘分区下标
	i = 0
	while i < len(p):
		# 找到符合条件的磁盘
		while dIndex < len(d) and p[i] > d[dIndex]:
			dIndex += 1
		# 没有可用的磁盘
		if dIndex >= len(d):
			return False
		# 给分区分配磁盘
		d[dIndex] -= p[i]
		i += 1
	return True
if __name__ == "__main__":
	d = [120,120,120]               # 磁盘
	p = [60,60,80,20,80]            # 分区
	if is_allocable(d,p):
		print("分配成功")
	else:
		print("分配失败")