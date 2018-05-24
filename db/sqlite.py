# -*- coding: utf-8 -*-
import os,sqlite3
db_file = os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
users = [('A-001', 'Adam', 95),
         ('A-002', 'Bart', 62),
         ('A-003', 'Lisa', 78)]
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
# cursor.executemany(r"insert into user values(?,?,?)",users)
def get_score_in(low,high):
	try:
		cursor.execute(r"select name from user where score>=? and score<=? order by score",(low,high))
		values = cursor.fetchall()
		name = [t[0] for t in values]
		print('get_score_in(%s,%s) == %s, get_score_in(%s,%s)' % (low,high,name,low,high))
	finally:
		cursor.close()
		conn.close()
	return name

# get_score_in(80, 95) 
# get_score_in(60, 80) 
get_score_in(60, 100)