#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Field(object):
	"""docstring for Field"""
	def __init__(self, name,column_type):
		self.name = name
		self.column_type = column_type
	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__,self.name)
class StringField(Field):
	"""docstring for StringField"""
	def __init__(self, name):
		super(StringField, self).__init__(name,'varchar(100)')
class IntegerField(Field):
	"""docstring for IntegerField"""
	def __init__(self, name):
		super(IntegerField, self).__init__(name,'bigint')
						
class ModelMetaclass(type):
	"""docstring for ModelMetaclass"""
	def __new__(cls, name,bases, attrs):
		if(name == "Model"):
			return type.__new__(cls,name,bases,attrs)
		print('Found Model: %s' % name)
		mappings = dict()
		for k,v in attrs.items():
			if isinstance(v,Field):
				print('Found mappings:%s==>%s' % (k,v))
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings
		attrs['__table__'] = name
		return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
		"""docstring for Model"""
		def __init__(self, **kw):
			super(Model, self).__init__(**kw)
		def __getattr__(self,key):
			try: 
				return self[key]
			except KeyError: 
				raise AttributeError(r"'Model' object has no attribute '%s'" % key)
		def __setattr__(self,key,value):
			self[key] = value
		def save(self):
			fields = []
			params = []
			args = []
			for k,v in self.__mappings__.items():
				fields.append(v.name)
				params.append('?')
				args.append(getattr(self,k,None))
			sql = 'insert into %s (%s) values(%s)' % (self.__table__,','.join(fields),','.join(params))
			print('SQL: %s' % sql)
			print('ARGS: %s' % str(args))

class User(Model):
	"""docstring for User"""
	id = IntegerField("id")
	name = StringField("name")
	email = StringField("email")
	password = StringField("password")
u = User(id=12,name='Twittytop',email='1690542111@qq.com',password='root')
u.save()		

