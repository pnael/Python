#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib

url = 'search.twitter.com'

t = httplib.HTTPConnection(url)
t.request("GET", "search.json?q=chamb%C3%A9ry")

r = t.getresponse()

print r.read()
