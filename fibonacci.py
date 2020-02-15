#!/usr/bin/env python
# Petit programme qui calcule la suite de Fibonacci

a,b = 0,1

while a < 1000:
    print(a, end=",")
    a,b = b, a+b
print()
