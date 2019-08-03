#!/usr/bin/env python

if __name__ == "__main__":
    a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
    s = "mont"

i = 0
while i < len(a) and (a[i][:len(s)]) != s:
    i = i + 1
print a[i]
