#!/usr/bin/env python

s = raw_input()
i = 0
while i < len(s) and (s[i] < "A" or "Z" < s[i]):
    i = i + 1
if i < len(s):
    j = i
    while j < len(s) and ("A" <= s[j] and s[j] <= "Z"):
        j = j + 1
if i < len(s):
    print s[i:j], i
