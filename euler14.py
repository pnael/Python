#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def Collatz(s):
    #n → n/2 (n is even)
    #n → 3n + 1 (n is odd)
    if n % 2 ==0:
        return n/2
    else:
        return 3*n+1

if __name__=="__main__":

    n=13
    maxi=1000000
    l=(0,0)
    for i in range(maxi,1,-1):
        j=0
        n=i
        while n != 1:
            j=j+1
            n = Collatz(n)
        if i % 10000 == 0:
            print(l)
        if (j,i)>l:
            l=(j,i)

    print(l)
