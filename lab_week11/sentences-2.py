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
        s[j] = s[j][0].capitalize() + s[j][1:]
        print " ".join(s[j:i + 1])
        j = i + 1

    i = i + 1
