#!/usr/bin/env python

if __name__ == "__main__":
    a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]
i = 0
t = 0
total = 10000000000
while i < len(a):
    if a[i] < total:
        total = a[i]
    i = i + 1
while t < len(a) and a[t] != total:
    t = t + 1
print t
