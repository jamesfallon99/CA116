#!/usr/bin/env python

import sys

n = int(sys.argv[1])
s = raw_input()

j = 0
i = 0
while i < n:
    while j < len(s) and s[j] != ",":
        j = j + 1

    j = j + 1
    i = i + 1

k = j + 1
while k < len(s) and s[k] != ",":
    k = k + 1

print s[j:k]
