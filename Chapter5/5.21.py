# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/15 9:14
Project:AlgorithmBook
Filename:5.21.py
"""

"""
如何截取包含中文的字符串
题目描述：编写一个截取字符串的函数，输入为一个字符串和字节数，输出为按字节数截取的字符串。
输入：“人ABC”4
输出：“人AB”
"""

def isChinese(c):
	return True if c >= u'u4e00' and c <= u'u9fa5' else False

def truncateStr(strs,lens):
	if strs == None or strs == "" or lens == 0:
		return ""
	chrArr = strs
	sb = ""
	count = 0                                   # 用来记录当前截取字符的长度
	for cc in chrArr:
		if count < lens:
			if isChinese(cc):
				# 如果要求截取子串的长度只差1个或者2个字符，但是接下来的字符是中文，
				# 那么截取结果子串中不保存这个中文字符
				if count+1 <= lens and coun+3 > lens:
					return sb
				count += 3
				sb += cc
			else:
				count += 1
				sb += cc
		else:
			break
	return sb

if __name__ == "__main__":
	sb = "人 ABC 们 DEF"
	#sb_unicode = unicode(sb,'utf8')
	print(truncateStr(sb,6))