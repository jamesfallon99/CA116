#!/usr/bin/env python

if __name__ == "__main__":
    a = [8, 9, 4, 7, 2, 11]
    i = 1
    j = 2

tmp = a[j]
a[j] = a[i]
a[i] = tmp
