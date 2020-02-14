#!/usr/bin/python

import random
import time


def SortAndCount(a,n):
    if n==1:
        return a,0
    else:
        b,x = SortAndCount(a[:n/2],len(a[:n/2]))
        #print "SortAndCount(",a[:n/2],len(a[:n/2]),") retourne ",b,x
        c,y = SortAndCount(a[n/2:],len(a[n/2:]))
        #print "SortAndCount(",a[n/2:],len(a[n/2:]),") retourne ",c,y
        d,z = mergeSortCountSplitInv(a,b,c,n)
        #print "MergeSortCountSplitIn((",a,b,c,n,") retourne ",d,z
        #print "***"
    return d,x+y+z

def mergeSortCountSplitInv(a,b,c,n):
    #merge aleft & aright
    d=[]
    i=j=k=inv=0
    for k in range(len(a)):
        try:
            if b[i]<c[j]:
                d.append(b[i])
                i=i+1
            elif b[i]>c[j]:            
                d.append(c[j])
                j=j+1
                inv=inv+(len(b)-i)
        except:
            if  j <len(c):
                #b est vide on ajoute c
                d[k:]=c[j:]
            elif i <len(b):
                #c est vide on ajoute b
                d[k:]=b[i:]
            else:
                #les deux sont vides
                return d,inv
            break
        #print d,inv
    return d,inv


a=[]
#initialize
f= open("IntegerArray.txt","r")
lines = f.readlines()
for line in lines:
    t = int(line)
    a.append(t)

#a = [3,2,1]

# measure process time : Python sort
t0 = time.clock()
d,b= SortAndCount(a,len(a))
print b," inversions"
print time.clock() - t0, "seconds process time"


