#!/usr/bin/env python

import sys
total = 0
i = 1
while i < len(sys.argv):
    s = sys.argv[i]
    with open(s) as f:
        s = f.read().split()
        j = 0
        while j < len(s):
            total = total + int(s[j])
            j = j + 1
    i = i + 1
print total
