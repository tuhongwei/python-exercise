class Chain(object):
	"""docstring for Student"""
	def __init__(self, path=''):
		self._path = path
	def __getattr__(self,path):
		return Chain('%s/%s' % (self._path,path))
	def __call__(self,*path):
		paths = ''
		for p in path:
			paths += ('/%s' % p);
		return Chain('%s%s' % (self._path,paths))
	def __str__(self):
		return self._path
	__repr__ = __str__
print(Chain().users('Twittytop','Lizzy').repos)

		