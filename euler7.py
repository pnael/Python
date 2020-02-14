#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def isPrime(n):
    #return True if N is prime, esle False

    #if < 2 not prime
    if n<2:
        return False

    # 2 is a prime
    if n == 2:
        return True

    #even number is not a prime
    if n % 2 == 0:
        return False

    #we test all the number till the square root of n
    max = int(math.ceil(math.sqrt(n)))
    for i in range(3,max+1):
        if n % i ==0:
            return False

    #no match so it is a prime
    return True


if __name__=="__main__":

    max =10001
    i=1
    c=0
    found = False

    while not found:
        i=i+1
        if isPrime(i):
            c=c+1
            print(c,i)
        if c == max:
            found = True
