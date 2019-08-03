#!/usr/bin/env python

header = raw_input()

s = raw_input()
count = 0
while s != "end":
    i = 0
    while i < len(s) and s[i] != ",":
        i = i + 1
    if s[i + 1:i + 3] == "WI":
        count = count + 1
    print count
    s = raw_input()
