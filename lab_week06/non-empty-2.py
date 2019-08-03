#!/usr/bin/env python

if __name__ == "__main__":
    a = ["", "dog", "", "", "", ""]

i = 0
while i < len(a) and a[i] == "":
    i = i + 1
if i < len(a):
    print a[i]
