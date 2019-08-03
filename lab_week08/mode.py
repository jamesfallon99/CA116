#!/usr/bin/env python

a = []
line = raw_input()
while line != "end":
    a.append(int(line))
    line = raw_input()

i = 1
while i < len(a):
    v = a[i]
    j = i
    while 0 < j and v < a[j - 1]:
        a[j] = a[j - 1]
        j = j - 1
    a[j] = v

    i = i + 1

value = 0
length = 0

i = 0
while i < len(a):
    j = i
    while j < len(a) and a[j] == a[i]:
        j = j + 1
    if length < j - i:
        value = a[i]
        length = j - i
    i = j

print value, length
