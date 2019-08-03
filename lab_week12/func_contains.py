#!/usr/bin/env python

from func_bsearch import bsearch

def contains(a, q):
    ind = bsearch(a, q)
    return 0 <= ind < len(a) and a[ind] == q

if __name__ == "__main__":
    print contains([2, 3, 6, 6, 7, 8], 2)
