#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

"""
This program print the ascii code it get from the command line
"""

import sys
import telnetlib
import re
from optparse import OptionParser

def main():

	if not sys.argv[1:]:
		sys.stdout.write("Sorry: you must specify at least an argument, ")
		sys.exit(0)


	for x in sys.argv[1:]:
		print(chr(int(x)+64))


    # THE program :-)
if __name__ == '__main__':
	main()
