#!/usr/bin/python
# -*- coding: utf-8 -*-

import math


if __name__=="__main__":
    sum=0
    
    max = 1000
    for i in range(2,max):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i

print(sum)
