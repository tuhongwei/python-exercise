try:
	f = open('index.php','r+',encoding='utf-8',errors='ignore')
	print(f.read())
finally:
	if f:
		f.close()
# 和下面等价
# with open('index.php','r+') as f:
# 	ptint(f.read())
