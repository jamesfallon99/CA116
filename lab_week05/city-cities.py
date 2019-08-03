#!/usr/bin/env python

header = raw_input()
s = raw_input()
while s != "end":
    i = 0
    while i < len(s) and s[i] != ",":
        i = i + 1
    if s[i - 4:i] == "City":
        print s[0:i]
    s = raw_input()
