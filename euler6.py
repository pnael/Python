#!/usr/bin/python
# -*- coding: utf-8 -*-



if __name__=="__main__":
    ssq=0
    sss=0
    for i in range(1,101):
        ssq=ssq+i*i
        sss=sss+i

print((sss*sss)-ssq)
