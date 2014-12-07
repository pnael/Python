#!/usr/bin/python
# Petit programme qui calcule la suite de Fibonacci
from math import sqrt

def Fib(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


for i in range(1,10):
    print(int(Fib(i)))

