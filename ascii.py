#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

"""
This program print the ascii code it get from the command line
"""

import sys
import telnetlib
import cStringIO
import re
from optparse import OptionParser

def main():

/// test
	if not sys.argv[1:]:
		sys.stdout.write("Sorry: you must specify at least an argument, ")
		sys.stdout.write("More help available with -h or --help option\n")
		sys.exit(0)

	parser = OptionParser()
	parser.add_option("-s", "--reverse",action="store", type="string", dest="restore",
			help="Convert char to ascii code.")
	parser.add_option("-d", "--debug",action="store_true", dest="debug",help="Set debug mode")
	(options, args) = parser.parse_args()

	for x in sys.argv[1:]:
		print chr(int(x)+64)


    # THE program :-)
if __name__ == '__main__':
	main()
