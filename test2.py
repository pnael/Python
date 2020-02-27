#!/usr/bin/env python
# Petit programme qui calcule la suite de Fibonacci


for n in range(2, 10):
   for x in range(2, n):
      if n % x == 0:
          print(n, 'equals', x, '*', n//x)
          break
   else:
          # loop fell through without finding a factor
          print(n, 'is a prime number')
