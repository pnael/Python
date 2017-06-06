#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

"""
Explain what program do.
"""

import getpass
import sys
import telnetlib
import cStringIO
import re
from optparse import OptionParser

def print_neighbours(neighbours,debug):
	cdpout = neighbours.splitlines()
	local_name = ''
	neighbour_name = ''
	neighbour_ip = ''
	both_ports =''
	
	for line in cdpout:
		if debug:
			print line
		# Le nom du switch	local
		m = re.match(r'\w+#',line)
		if m:
			local_name = line[:m.end()-1]
			
		
		# Le nom du switch	remote
		m = re.match('(Device ID: )',line)
		if m:
			neighbour_name = line[m.end():]
					
		#son IP
		m = re.match('(  IP address: )',line)
		if m:
			neighbour_ip = line[m.end():]
			
		#port 
		m = re.match('(Interface: )',line)
		if m:
			both_ports = line
		
		
		if neighbour_name and neighbour_ip and both_ports:
			print local_name+","+neighbour_name+","+neighbour_ip+","+both_ports
			neighbour_name = ''
			neighbour_ip = ''
			lboth_ports =''
			remote_port=''
		

def main():
	# Usual verifications and warnings
	user = "naelp"
	password = "stock01"
	
	if not sys.argv[1:]:
		sys.stdout.write("Sorry: you must specify at least an argument")
		sys.stdout.write("More help avalaible with -h or --help option")
		sys.exit(0)

	parser = OptionParser()
	parser.add_option("-s", "--switchname",action="store", type="string", dest="switchname",
			help="Cisco switch IP or hostname.")
	parser.add_option("-l", "--level",action="store", type="int", dest="level", default=1,
			help="Specify how many levels do we log, default is 1.")		
	parser.add_option("-d", "--debug",action="store_true", dest="debug",help="Set debug mode")		
	(options, args) = parser.parse_args() 

    # THE program :-)
   
	tn = telnetlib.Telnet(options.switchname)
	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
		tn.read_until("Password: ")
		tn.write(password + "\n")
	if options.debug:
		print "logged"
	tn.write("sh cdp neighbors detail\n")
	if options.debug:
		print "sh cdp neighbors detail\n"

	tn.write("\nexit\n")
	if options.debug:
		print "exit\n"	
	
	
	
	if options.debug:
		print "read neigbours"
	neighbours = tn.read_all()
		
	
	
	print_neighbours(neighbours,debug=options.debug)


if __name__ == '__main__':
    main()