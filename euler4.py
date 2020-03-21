#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def isPalindrome(s):
    #return True if s is a palindrime

    #if < 2 not prime
    if s == s[::-1]:
        return True
    else:
        return False

    #We should never reach here
    print("error in isPalindrome"=
    return False


if __name__=="__main__":
    r=[]

    for i in range(999,100,-1):
        for j in range(999,100,-1):
            t = i * j
            if isPalindrome(str(t)):
                r.append(t)

print(sorted(r))
