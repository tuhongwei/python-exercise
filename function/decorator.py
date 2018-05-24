import functools
def log(*text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('begin call')
			print('%s %s():' % (text,func.__name__))
			return_value = func(*args,**kw)
			print('end call')
			return return_value
		return wrapper
	return decorator
@log('excute')
def now():
	 print('2016-10-31')
now()
print(now.__name__)