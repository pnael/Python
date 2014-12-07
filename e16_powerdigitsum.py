#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__=="__main__":

    s = str(2**1000)
    r=0
    for c in s:
        i=int(c)
        r=r+i
    print(r)
