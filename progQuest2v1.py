#!/usr/bin/python

import random
import time


def QuickSort(a,n):
        if n==1:
                return a
        # choisir le pivot a l'avenir 
        p = 0
        
        print "Partition",a,p,len(a)-1
        a,p = Partition(a,p,len(a)-1)
        print a,p
        print "QuickSort ",a[0:p], p
        print "QuickSort ",a[p+1:len(a)], len(a)-p-1
        a = QuickSort(a[0:p],p)
        so = QuickSort(a[p+1:len(a)],len(a)-p-1)
        return a

def Partition(A,l,r):
        #  partition array A starting from l to r
        p=A[l]
        i=l+1
        for j in range(l+1,r+1):
                if A[j]<p:
                        A[j],A[i]=A[i],A[j]
                        i=i+1
        A[l],A[i-1]=A[i-1],A[l]
        return A,i-1

a=[]
#initialize
f= open("QuickSort.txt","r")
lines = f.readlines()
for line in lines:
    t = int(line)
    a.append(t)

a = [3,4,2,1]

# measure process time : Python sort
t0 = time.clock()
print a
#db,i = Partition(a,0,3)
db= QuickSort(a,len(a))
print db
print time.clock() - t0, "seconds process time"


