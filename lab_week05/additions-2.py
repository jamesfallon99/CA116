#!/usr/bin/env python

s = raw_input()
j = 0
i = 0
total = 0
while i < 5:
    k = j
    while k < len(s) and s[k] != "+":
        k = k + 1
    total = int(s[j:k]) + total
    j = k + 1
    i = i + 1
print total
