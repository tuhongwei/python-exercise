#!/user/bin/env python3
# -*- coding: utf-8 -*-
# L1 = ['adam', 'LISA', 'barT']变成首字母大写
def normalize(name):
	return str.capitalize(name)
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))
print(L2)
# 用lambda改写
L3 = list(map(lambda name: str.capitalize(name),L1))
print(L3)
# 自定义一个首字母大写的函数
def firstUpper(name):
	L = [c.lower() for c in name]
	L[0] = L[0].upper()
	return ''.join(L)
L4 = list(map(firstUpper,L1))
print(L4)

# reduce求积
from functools import reduce
def prod(L):
	return reduce(lambda x,y: x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce
def str2float(s):
	def char2num(ch):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[ch]
	def str2int(s):
		return reduce(lambda x,y: x*10+y,map(char2num,s))
	try:
		n = s.index('.')
		s = s[:n] + s[n+1:]
		return str2int(s)/pow(10,len(s)-n)
	except:
		return str2int(s)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))

# 另一种实现
from functools import reduce
def str2float2(s):
	def char2num(ch):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':-1}[ch]
	nums = map(char2num,s)
	point = 0
	def toFloat(x,y):
		nonlocal point
		if y== -1:
			point = 1
			return x
		if point==0:
			return x*10+y;
		else:
			point = point*10
			return x+y/point
	return reduce(toFloat,nums,0.0)
print(str2float2('0'))
print(str2float2('123.456'))
print(str2float2('123.45600'))
print(str2float2('0.1234'))
print(str2float2('.1234'))
print(str2float2('120.0034'))