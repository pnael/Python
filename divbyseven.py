#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = []
for number in range(2000,3200):
    if number % 7 == 0 and number % 5 != 0:
        l.append(str(number))
        
print(','.join(l)) 
