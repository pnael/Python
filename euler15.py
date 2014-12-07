#!/usr/bin/python
# -*- coding: utf-8 -*-

m=[]
n=[]
if __name__=="__main__":
    maxi = 20
    for i in range(maxi+1):
        m=[]
        for j in range(maxi+1):
            try:
                m.append(n[i-1][j]+m[j-1])
            except IndexError:
                m.append(1)
        n.append(m)
    print n
