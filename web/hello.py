def application(environ,start_response):
	start_response('200 ok',[('Content-Type','text/html')])
	body = '<h1>Hello %s!</h1>' % (environ['PATH_INFO'][2:4] or 'World')
	return [body.encode('utf-8')]