#!/usr/bin/python 

import random
import time


def mergeSort(a):
    if len(a)<=1:
        return a
    else:
        aleft = mergeSort(a[:len(a)/2])
        aright = mergeSort(a[len(a)/2+1:])
    #merge aleft & aright
    i=j=k=0
    for k in range(len(a)):
        try:
            if aleft[i]<aright[j]:
                a[k]=aleft[i]
                i=i+1
            elif aleft[i]>aright[j]:            
                a[k]=aright[j]
                j=j+1
            else:
                a[k]=aleft[i]
                i=i+1
                j=j+1
        except IndexError:
            if i>j:
                #aleft est vide on ajoute aright
                a[k:]=aright[j:]
            elif i<j:
                #aright est vide on ajout aleft
                a[k:]=aleft[i:]
            else:
                #les deux sont vides
                return a
            break
    return a

#initialization
a=[]
t0 = time.clock()
for i in range(10000000):
    a.append(random.randint(0,100000000))
print time.clock() - t0, "seconds initialize time"

max = len(a)
print max
print time.clock() - t0, "seconds init time"

# measure process time : Python sort
t0 = time.clock()
b= sorted(a)
print time.clock() - t0, "seconds process time"

# measure process time : merge sort
t0 = time.clock()
c= mergeSort(a)
print time.clock() - t0, "seconds process time"


