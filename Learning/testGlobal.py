#!/usr/bin/python
# -*- coding: utf-8 -*-

myGlobal = 1


def ChangeMyGlobal():
    global myGlobal
    myGlobal = 2

def PrintMyGlobal():
    print(myGlobal)

ChangeMyGlobal()
PrintMyGlobal()
