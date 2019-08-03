#!/usr/bin/env python

s = raw_input()
i = 0
while i < len(s) and s[i] == "0":
    i = i + 1
s = s[i:]

i = 0
while i < len(s) and s[i] != ".":
    i = i + 1
if len(s) <= i:
    s = s + "."

i = 0
while i < len(s) and s[len(s) - i - 1] == "0":
    i = i + 1
s = s[:len(s) - i]

if s[0] == ".":
    s = "0" + s

if s[len(s) - 1] == ".":
    s = s + "0"
print s
