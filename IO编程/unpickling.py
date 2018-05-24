import pickle

with open('dump.txt','rb') as f:
	d = pickle.load(f)
print(d)

import json 

with open('dump-json.txt','r') as f:
	d = json.load(f)
print(d)

