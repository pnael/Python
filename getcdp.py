#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

"""
This program connects to Cisco devices to get its CDP neighbours.
Then the results is printed in CSV format
"""

import getpass
import sys
import telnetlib
import cStringIO
import re
from optparse import OptionParser

def print_neighbours(tn,debug,level=0):
	local_name = ''
	neighbour_name = ''
	neighbour_ip = ''
	both_ports =''
	
	if debug:
		print "read neigbours"
	neighbours = tn.read_all()
	cdpout = neighbours.splitlines()
	
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
			neighbour_ip = None
			both_ports = None
								
		#son IP
		m = re.match('(  IP address: )',line)
		if m:
			neighbour_ip = line[m.end():]
			
		#port 
		m = re.match('(Interface: )',line)
		if m:
			both_ports = line
				
		if neighbour_name and neighbour_ip and both_ports:
			print local_name+","+both_ports+","+neighbour_name+","+neighbour_ip
			if level > 0:
				if debug:
					print "calling level ",(level-1)," for "+neighbour_ip
				tnt = cisco_connect(neighbour_ip,debug)
				print_neighbours(tnt,debug,level-1)
			neighbour_name = None

	
		
def	cisco_connect(switchip,debug):
	user = "naelp"
	password = "stock01"
	
	tn = telnetlib.Telnet(switchip)
	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
		tn.read_until("Password: ")
		tn.write(password + "\n")
	if debug:
		print "logged"
	tn.write("sh cdp neighbors detail\n")
	if debug:
		print "sh cdp neighbors detail\n"

	tn.write("\nexit\n")
	if debug:
		print "exit\n"	
	
	return tn
		
def main():
	# Usual verifications and warnings
	user = "naelp"
	password = "stock01"
	
	if not sys.argv[1:]:
		sys.stdout.write("Sorry: you must specify at least an argument")
		sys.stdout.write("More help avalaible with -h or --help option")
		sys.exit(0)

	parser = OptionParser()
	parser.add_option("-s", "--switchname",action="store", type="string", dest="switchip",
			help="Cisco switch IP or hostname.")
	parser.add_option("-l", "--level",action="store", type="int", dest="level", default=0,
			help="Specify how many levels do we log, default is 0, only current equipment neighbours.")		
	parser.add_option("-d", "--debug",action="store_true", dest="debug",help="Set debug mode")		
	(options, args) = parser.parse_args() 

    # THE program :-)
   
	tn = cisco_connect(options.switchip, options.debug)
	print_neighbours(tn,debug=options.debug,level=options.level)


if __name__ == '__main__':
    main()