#!/usr/bin/env python

import sys
s = sys.stdin.read().split()
d = {}
i = 0
while i < len(s):
    word = s[i]
    if word not in d:
        d[word] = 0
    d[word] = d[word] + 1
    i = i + 1
for word in d:
    if d[word] == 1:
        print word
