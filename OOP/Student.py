class Student(object):
	"""docstring for Student"""
	def __init__(self, name,score,*age):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s: %s'% (self.__name,self.__score))
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')
	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
bart = Student('Bart Simpson',59,9)
bart.age = 8
print(bart.age)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()
print(bart.get_grade())
print(lisa.get_score())

lisa.__name = 'New Name'
print(lisa.get_name())
