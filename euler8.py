#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

s ="""7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
"""


if __name__=="__main__":

    a = None
    b = None
    c = None
    d = None
    e = None
    f = None
    g = None
    h = None
    i = None
    j = None
    k = None
    l = None
    m = None
    max = -1

    while s :
        try:
            a=int(s[0])
            b=int(s[1])
            c=int(s[2])
            d=int(s[3])
            e=int(s[4])
            f=int(s[5])
            g=int(s[6])
            h=int(s[7])
            i=int(s[8])
            j=int(s[9])
            k=int(s[10])
            l=int(s[11])
            m=int(s[12])
        except:
            break

        r= a*b*c*d*e*f*g*h*i*j*k*l*m
        if r>max:
            max=r
        print(a,b,c,d,e,f,g,h,i,j,k,l,m,r)
        s=s[1:]


print(max)
