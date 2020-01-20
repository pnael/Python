#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import httplib

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 2:
      print(sys.argv)
      twitsearch  = sys.argv[1]
      print(twitsearch)
url = 'search.twitter.com'

t = httplib.HTTPConnection(url)
t.request("GET", "search.json?q="+twitsearch)

r = t.getresponse()

print r.read()
