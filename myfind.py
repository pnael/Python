#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def GetArgs():
    print(sys.argv)
    return sys.argv[1]

if __name__== '__main__':
    path = GetArgs()
    print(path)
