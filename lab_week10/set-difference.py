#!/usr/bin/env python

import sys
with open("a.txt", "r") as f:
    a = f.read().split()

da = {}
i = 0
while i < len(a):
    word_a = a[i]
    da[word_a] = None
    i = i + 1

with open("b.txt", "r") as f:
    b = f.read().split()

db = {}
j = 0
while j < len(b):
    word_b = b[j]
    db[word_b] = None
    j = j + 1

for word in da:
    if word not in db:
        print word
