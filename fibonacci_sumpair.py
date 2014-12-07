#!/usr/bin/python
# Petit programme qui calcule la suite de Fibonacci
from math import sqrt

max = 4000000
r=[]

def Fib(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


for i in range(1,max):
    a = int(Fib(i))
    if a > max:
        break
    if a % 2==0:
        print(a)
        r.append(a)

print("****")
print (sum(r))

