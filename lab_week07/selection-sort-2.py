#!/usr/bin/env python

s = raw_input()
i = 0
a = []
while s != "end":
    a.append(int(s))
    s = raw_input()

i = input()
j = i + 1
while j < len(a):
    if a[j] < a[i]:
        i = j
    j = j + 1
print i
