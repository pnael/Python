#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
n = int(input("Dict till :"))
d = dict()

for i in range(1,n+1):
    d[i] = i * i

print(d)
