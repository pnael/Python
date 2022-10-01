#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def permut(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permut(together, letter + pocket)

print(permut("ABCD", ""))
