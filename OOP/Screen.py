class Screen(object):
	"""docstring for Screen"""
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,width):
		if not isinstance(width,int):
			raise ValueError('width must be an integer!')
		elif width < 0:
			raise ValueError('width must be positive number!')
		else:
			self._width = width
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,height):
		if not isinstance(height,int):
			raise ValueError('height must be an integer!')
		elif height < 0:
			raise ValueError('height must be positive number!')
		else:
			self._height = height
	@property
	def resolution(self):
		return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %s ?' % s.resolution
	
	
		