import logging
logging.basicConfig(level=logging.INFO) #错误级别 debug info warning error

s = '0'
n = int(s)
logging.error('n = %d' % n)
print(10/n)