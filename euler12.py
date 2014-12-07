#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def getTriangleNumber(s):
    t=0
    for i in range(s+1):
        t=t+i
    return t

if __name__=="__main__":

    found=False
    i=2
    while not found:
        t=getTriangleNumber(i)
        c=0
        maxi = int(math.sqrt(t/2))+1
        for j in range(1,maxi):
            if t % j ==0:
                c=c+2
            if c>=500:
                print("Found ",t)
                found=True
        if i % 100 == 0:
            print(i,t,c)
        i=i+1
