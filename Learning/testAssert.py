#!/usr/bin/python
# -*- coding: utf-8 -*-

x = 1
assert x > 0, 'x is less than zero'

print x
for x in range(5,-5,-1):
    assert x > 0, 'x is less than zero'
    print x
