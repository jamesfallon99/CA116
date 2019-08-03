#!/usr/bin/env python

if __name__ == "__main__":
    a = ["cat", "ele", "mouse", "liz", "horse", "mong"]

i = 0
while i < len(a) and 6 > len(a[i]):
    i = i + 1
if i < len(a):
    print a[i]
