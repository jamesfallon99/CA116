#!/usr/bin/env python

s = raw_input()
i = 0
while i < len(s) and ("0" > s[i] or "9" < s[i]):
    i = i + 1
if i < len(s):
    j = i
    while j < len(s) and ("0" < s[j] and "9" > s[j]):
        j = j + 1
        if j < len(s):
            k = j
            while k < len(s) and ("0" > s[k] or "9" < s[k]):
                k = k + 1
                if k < len(s):
                    l = k
                    while l < len(s) and ("0" < s[l] and "9" > s[l]):
                        l = l + 1
                        if l < len(s):
                            print s[k:l], k
