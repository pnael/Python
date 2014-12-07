#!/usr/bin/python
# -*- coding: utf-8 -*-


max = 1000
r = []

for i in range(1,max):
   if not i % 3:
        r.append(i)
        continue
   if not i % 5:
        r.append(i)

print(sum(r))
