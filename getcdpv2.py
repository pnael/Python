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

def print_neighbours(tn,username,password,debug,level=0):
	local_name = ''
	neighbour_name = ''
	neighbour_ip = ''
	both_ports =''
	
	try:
		tn.write("sh cdp neighbors detail\n")
		tn.write("\nexit\n")
		if debug:
			print "sh cdp neighbors detail\n"
	except:
		#not connected, wrong password
		return
		
	neighbours = tn.read_all()
	cdpout = neighbours.splitlines()
	
	for line in cdpout:
		if debug:
			pass
			#print line
		
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
					print level-1
					print neighbour_ip
					print username
					print "calling level ",str(level-1)," for "+neighbour_ip+" "+"with username "+username+"\n"
				tnt = cisco_connect(neighbour_ip,username, password, debug)
				print_neighbours(tnt,username, password, debug,level-1)
			neighbour_name = None

	
		
def	cisco_connect(switchip, user, password, debug):
	
	
	try:
		tn = telnetlib.Telnet(switchip)
	except:
		print("Error at connecting to "+switchip+"\n")
		exit()
		
	tn.read_until("User")
	tn.write(user + "\n")
	if password:
		tn.read_until("Password: ")
		tn.write(password + "\n")
	if debug:
		print "logged"
	
	#tn.write("sh cdp neighbors detail\n")
	#if debug:
	#	print "sh cdp neighbors detail\n"

	#tn.write("\nexit\n")
	#if debug:
	#	print "exit\n"	
	
	return tn
		
def main():
	# Usual verifications and warnings
	user = "naelp"
	password = "xxx"
	
	if not sys.argv[1:]:
		sys.stdout.write("Sorry: you must specify at least an argument")
		sys.stdout.write("More help avalaible with -h or --help option")
		sys.exit(0)

	parser = OptionParser()
	parser.add_option("-s", "--switchname",action="store", type="string", dest="switchip",
			help="Cisco switch IP or hostname.")
	parser.add_option("-l", "--level",action="store", type="int", dest="level", default=0,
			help="Specify how many levels do we log, default is 0, only current equipment neighbours.")
	parser.add_option("-u", "--username",action="store", type="string", dest="username", default="",
			help="Telnet username")
	parser.add_option("-p", "--password",action="store", type="string", dest="password", default="",
			help="Telnet password")			
	parser.add_option("-d", "--debug",action="store_true", dest="debug",help="Set debug mode")		
	(options, args) = parser.parse_args() 

    # THE program :-)
   
	tn = cisco_connect(options.switchip, options.username, options.password, options.debug)
	print_neighbours(tn,options.username,options.password,debug=options.debug,level=options.level)
	
	#Leaving
	tn.close()


if __name__ == '__main__':
    main()
