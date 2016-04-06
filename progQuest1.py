#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import time

a=[]

f= open("IntegerArray.txt","r")
lines = f.readlines()
for line in lines:
    t = int(line)
    a.append(t)

i=j=nbi=0

# measure process time : Python sort
t0 = time.clock()
for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                nbi=nbi+1
print time.clock() - t0, "seconds process time"
print nbi
