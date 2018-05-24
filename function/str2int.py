from functools import reduce
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(char):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[char]
	return reduce(fn,map(char2num,s))
print(str2int('1579'))
# 用lambda函数简化
from functools import reduce
def str2int2(s):
	def char2num(char):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[char]
	return reduce(lambda x,y: x*10+y,map(char2num,s))
print(str2int2('2468'))

