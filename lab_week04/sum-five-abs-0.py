#!/usr/bin/env python

total = 0
n = input()
while n != 0:
   if n < 0:
      n = n * - 1
   total = n + total
   n = input()
print total
