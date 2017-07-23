#!/usr/bin/python
# -*- coding: utf-8 -*-


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file,to_file)
out_file = open(to_file, "w").write(open(from_file).read())

