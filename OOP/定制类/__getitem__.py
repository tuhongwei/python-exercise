class Fib(object):
	"""docstring for Fib"""
	def __getitem__(self, n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		elif isinstance(n,slice):
			start = n.start or 0
			stop = n.stop
			step = n.step or 1
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
					start += step
				a,b = b,a+b
			return L
f = Fib()
print(f[:8:2])
