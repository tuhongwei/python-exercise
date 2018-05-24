#!/user/bin/env python3
# _*_ coding: utf-8 _*_
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0);
        L = [L[i-1] + L[i] for i in range(len(L))]
n = 0
from collections import Iterable
from collections import Iterator
print(isinstance(triangles(),Iterable))
print(isinstance(triangles(),Iterator))
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        print(type(t))
        break
print(isinstance(iter({}),Iterator))
