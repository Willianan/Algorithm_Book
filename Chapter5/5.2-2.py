# -*- coding:utf-8 -*-
"""
Author：Charles Van
E-mail:  williananjhon@hotmail.com
Time：2019/3/6 9:10
Project:AlgorithmBook
Filename:5.2-2.py
"""

# 方法二：滑动比较法
def getMaxSubStr(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	maxLen = 0
	tmpmaxLen = 0
	maxLenEnd = 0
	sb = ''
	i = 0
	while i < len1 + len2:
		s1begin = s2begin = 0
		tmpmaxLen = 0
		if i < len1:
			s1begin = len1 - i
		else:
			s2begin = i - len1
		j = 0
		while (s1begin + j < len1) and (s2begin + j < len2):
			if list(s1)[s1begin+j] == list(s2)[s2begin+j]:
				tmpmaxLen += 1
			else:
				if tmpmaxLen > maxLen:
					maxLen = tmpmaxLen
					maxLenEnd = s1begin + j
				else:
					tmpmaxLen = 0
			j += 1
		if tmpmaxLen > maxLen:
			maxLen = tmpmaxLen
			maxLenEnd = s1begin + j
			i += 1
	i = maxLenEnd - maxLen
	while i < maxLenEnd:
		sb = sb + list(s1)[i]
		i += 1
	return sb



if __name__ == "__main__":
	str1 = "abcade"
	str2 = "dgcadde"
	print(getMaxSubStr(str1,str2))