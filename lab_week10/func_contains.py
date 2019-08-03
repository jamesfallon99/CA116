#!/usr/bin/env python

import func_bsearch

def contains(a, q):
    s = func_bsearch.bsearch(a, q)


func_bsearch.bsearch([2,3,6,6,7,8], 1)
func_bsearch.bsearch([2,3,6,6,7,8], 2)
func_bsearch.bsearch([2,3,6,6,7,8], 6)
func_bsearch.bsearch([2,3,6,6,7,8], 8)
func_bsearch.bsearch([2,3,6,6,7,8], 9)
func_bsearch.bsearch([2,3,6,6,7,8], 4)