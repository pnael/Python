#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)

x=int(input())
print(fact(x))
