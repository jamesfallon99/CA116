#!/usr/bin/env python

import sys
with open("a.txt", "r") as f:
    a = f.read().split()

d = {}
i = 0
while i < len(a):
    words_a = a[i]
    if words_a not in d:
        d[words_a] = True
    i = i + 1

with open("b.txt", "r") as f:
    b = f.read().split()
j = 0
while j < len(b):
    words_b = b[j]
    if words_b not in d:
        d[words_b] = True
    j = j + 1

for words in d:
    print words
