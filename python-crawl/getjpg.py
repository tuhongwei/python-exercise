#!/user/bin/dev python3
#-*- coding: utf-8 -*-
from urllib import request,parse
import re
def getHtml(url):
	print('Login to weibo.cn...')
	email = input('Email: ')
	password = input('Password: ')
	login_data = parse.urlencode([
		('username',email),
		('password',password),
		('entry','mweibo.cn'),
		('client_id',''),
		('savestate', '1'),
	    ('ec', ''),
	    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
	])
	req = request.Request(url)
	req.add_header('Origin','https://passport.weibo.cn')
	req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
	req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
	page = request.urlopen(req,data=login_data.encode('utf-8'))
	print(page.status,page.reason)
	for k,v in page.getheaders():
		print('%s: %s' % (k,v))
	html = page.read()
	return html
def getImg(html):
	reg = 'src="(.+\.jpg)"'
	imgre = re.compile(reg)
	html = html.decode('utf-8')
	# print('Data:',html)
	imglist = re.findall(imgre,html)
	n = 0
	for imgurl in imglist:
		request.urlretrieve(imgurl,'%s.jpg' % n)
		n += 1
html = getHtml("https://passport.weibo.cn/sso/login")
