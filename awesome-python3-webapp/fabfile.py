#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Twittytop'

'''
Deployment toolkit.
'''

import os,re
from datetime import datetime

# 导入Fabric API:
from fabric.api import *

env.user = 'xiaoyun'
env.sudo_user = 'root'
env.hosts = ['60.205.200.148']

db_user = 'root'
db_password = 'root'

_TAR_FILE = 'dist-awesome-tar.gz'
_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE
_REMOTER_BASE_DIR = '/usr/share/nginx/html/awesome-python3-webapp'

def _current_path():
	return os.path.abspath('.')

def _now():
	return datetime.now().strftime('%y-%m-%d_%H.%M.%S')

def build():
	'''
	Build dist package.
	'''
	includes = ['static','templates','transwarp','favicon.ico','*.py']
	excludes = ['test','.*','*.pyc','*.pyo']
	local('rm -f dist/%s' % _TAR_FILE)
	with lcd(os.path.join(_current_path(),'www')):
		cmd = ['tar','--dereference','-czvf','../dist/%s' % _TAR_FILE]
		cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
		cmd.extend(includes)
		local(' '.join(cmd))

def deploy():
	newdir = 'www-%s' % _now()
	run('rm -f %s' % _REMOTE_TMP_TAR)
	put('dist/%s' % _TAR_FILE,_REMOTE_TMP_TAR)
	with cd(_REMOTER_BASE_DIR):
		sudo('mkdir %s' % newdir)
	# 解压到新目录
	with cd('%s/%s' % (_REMOTER_BASE_DIR,newdir)):
		sudo('tar -xzvf %s' % _REMOTE_TMP_TAR)
	# 重置软链接
	with cd(_REMOTER_BASE_DIR):
		sudo('rm -f www')
		sudo('chown root:root www')
		sudo('chown -R root:root %s' % newdir)
	# 重启Python服务和nginx服务器:
	with settings(warn_only=True):
		sudo('supervisorctl stop awesome')
		sudo('supervisorctl start awesome')
		sudo('/etc/init.d/nginx reload')
