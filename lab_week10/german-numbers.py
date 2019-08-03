#!/usr/bin/env python

import sys
eng = sys.stdin.read().split()

german = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn",
}
i = 0
while i < len(eng):
    english = eng[i]
    print german[english]
    i = i + 1
