#!/usr/bin/env python

def bsearch(a, q):
    low = 0
    high = len(a)
    while low < high:
        mid = (low + high) / 2
        if a[mid] < q:
            low = mid + 1
        else:
            high = mid
    return low
print bsearch([2,3,6,6,7,8], 1)
print bsearch([2,3,6,6,7,8], 2)
print bsearch([2,3,6,6,7,8], 4)
print bsearch([2,3,6,6,7,8], 6)
print bsearch([2,3,6,6,7,8], 8)
print bsearch([2,3,6,6,7,8], 9)