#!/usr/bin/python
# -*- coding: utf-8 -*-



if __name__=="__main__":
    s=[]
    j=2520
    found = False
    while not found:
        for i in range(20,2,-1):
            if j % i != 0:
                found = False
                break
            found = True
        if found:
            break
        if j % 1000000==0:
            print(j)
        j=j+1
print(j)
