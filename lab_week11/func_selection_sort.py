#!/usr/bin/env python

def selection_sort(a):
    i = 0
    while i < len(a):
        p = i
        j = i + 1
        while j < len(a):
            if a[j] < a[p]:
                tmp = a[p]
                a[p] = a[j]
                a[j] = tmp
            j = j + 1
        i = i + 1
