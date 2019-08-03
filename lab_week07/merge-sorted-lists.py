#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()
b = []
t = raw_input()
while t != "end":
    b.append(int(t))
    t = raw_input()

i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        print a[i]
        i = i + 1
    else:
        print b[j]
        j = j + 1

while i < len(a):
    print a[i]
    i = i + 1
while j < len(b):
    print b[j]
    j = j + 1
