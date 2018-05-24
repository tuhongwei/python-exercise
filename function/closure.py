def calc_sum(*args):
	def lazy_sum():
		s = 0
		for n in args:
			s = s + n
		return s
	return lazy_sum
f = calc_sum(1,3,5,7,9)

def count():
	fs = []
	for i in range(1,4):
		fs.append(lambda i=i: i*i)# lambda函数简化
	return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())
