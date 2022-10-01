#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(x):
    if x == 1:
        return x
    return x * fact(x-1)

print("Factorielle de:")
x=int(input())
print(fact(x))
