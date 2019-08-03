#!/usr/bin/env python

with open("a.txt") as f:
    a = f.read().split()

da = {}
i = 0
while i < len(a):
    da[a[i]] = True
    i = i + 1

with open("b.txt") as f:
    a = f.read().split()

db = {}
i = 0
while i < len(a):
    db[a[i]] = True
    i = i + 1
for word in da:
    if word in db:
        print word
