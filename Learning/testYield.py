#!/usr/bin/python
# -*- coding: utf-8 -*-

def gen_integer(r):
    for i in range(r):
        yield i


gen = gen_integer(5)

print(gen.next())
print(gen.next())
print(gen.next())
