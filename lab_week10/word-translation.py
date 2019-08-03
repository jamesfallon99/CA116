#!/usr/bin/env python

import sys
s = sys.stdin.read().split()
d = {}
i = 0
with open("translation.txt", "r") as f:
    a = f.read().split()
    while i < len(a):
        k = a[i]
        if k not in d:
            d[k] = a[i + 1]
        i = i + 2

i = 0
while i < len(s):
    english = s[i]
    print d[english]
    i = i + 1
