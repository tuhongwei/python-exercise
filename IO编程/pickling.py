import pickle

d = dict(name='Bob',age=20,score=90)
with open('dump.txt','wb') as f:
	pickle.dump(d,f)

import json

d = dict(name='Bob',age=20,score=90)
with open('dump-json.txt','w') as f: 
	json.dump(d,f)
# print(json.dumps(d))