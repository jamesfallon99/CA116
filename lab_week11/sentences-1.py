#!/usr/bin/env python

import sys
s = sys.stdin.read().split()
i = 0
j = 0
d = {
    "!": True,
    ".": True,
    "?": True
}
while i < len(s):
    if s[i][len(s[i]) - 1] in d:
        print " ".join(s[j:i + 1])
        j = i + 1

    i = i + 1
