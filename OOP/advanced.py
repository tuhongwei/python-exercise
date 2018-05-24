class Student(object):
	"""docstring for Student"""
	pass

def set_age(self,age):
	self.age = age
s1 = Student()
from types import MethodType
# 给实例s1绑定方法，实例s2没有
s1.set_age = MethodType(set_age,s1)
s1.set_age(29)
print(s1.age)
s2 = Student()
# print(s2.age)

# 给所有实例绑定方法
Student.set_age = set_age
s2.set_age(35)
print(s2.age)
