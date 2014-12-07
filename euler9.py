#!/usr/bin/python
# -*- coding: utf-8 -*-


def isPythTriplet(a,b,c):
    if a > b:
        return False
    if b > c:
        return  False

    if (a*a)+(b*b)==(c*c):
        return True
    else:
        return False


if __name__=="__main__":

    a=1
    b=2
    c=3
    print(a,b,c,isPythTriplet(a,b,c))
    a=3
    b=4
    c=5
    print(a,b,c,isPythTriplet(a,b,c))

    for i in range(500):
        for j in range(500):
            for k in range(500):
                if i+j+k==1000 and isPythTriplet(i,j,k):
                    print("ok",i,j,k,i+j+k,i*j*k)
                    

