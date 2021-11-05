#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def square(x):
    result = {}
    for i in range(1,x+1):
        result[i]=i*i
    return result

x=int(input())
print(square(x))
