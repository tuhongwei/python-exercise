# -*- coding: utf-8 -*-
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按名字排序
def by_name(t):
	return t[0]
print(sorted(L,key=by_name))
# 按分数排序
def by_score(t):
	return t[1]
print(sorted(L,key=by_score,reverse=True))