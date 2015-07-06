#!/usr/bin/python
# -*- coding: utf-8 -*-

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

class newSwitch:
    def __init__(self,ip,username='',password='',debug=False):
        
        self.username = username
        self.password = password
        self.ip = ip
        try:
            self.tn = self.cisco_connect(self.ip, debug)
        except:
            if debug:
                print "Exception while connecting to",self.ip, " with ",self.username
            raise
        self.neighbourName = {}
        
        
        
    def cisco_connect(self,switchip,  debug):
    # connect to a cisco switch thorugh Telnet and tacacs account
    
        username = self.username
        password = self.password
        
        try:
            tn = telnetlib.Telnet(switchip)
        except:
            if (debug):
                print("Error at connecting to "+switchip+"\n")
            raise
        
        if debug:
            print "Trying username",type(username), username
        tn.read_until("User")
        tn.write(username + "\n")
       
        if debug:
            print "Trying password", type(password), password
        tn.read_until("Password: ")
        tn.write(password + "\n")
        
        if debug:
            print "logged"

        return tn
        
    def getNeighbours(self,debug=False):
    # Get netighbours using sh cdp neighbors detail
    # parse the output to fill in the array of neighbours self.neghbourName
        self.localName = ''
        neighbour_name = ''
        neighbour_ip = ''
        both_ports =''
        tn = self.tn

        # send command to get neighbours
        try:
            tn.write("term len 0\n");
            tn.write("sh cdp neighbors detail\n")
            tn.write("\nexit\n")
            if debug:
                print "sh cdp neighbors detail\n"
        except:
            #not connected, 
            raise
            return
            
        # read neighbours
        neighbours = tn.read_until("exit")
        cdpout = neighbours.splitlines()
       
        for line in cdpout:
            if debug:
                print line
        
            # Le nom du switch    local
            m = re.match(r'\w+#',line)
            if m:
                self.localName = line[:m.end()-1]
                if debug: print "get localname",self.localName
            
            # Le nom du switch    remote
            m = re.match('(Device ID: )',line)
            if m:
                neighbour_name = line[m.end():]
                neighbour_ip = None
                both_ports = None
                if debug: print "get remote name",neighbour_name
                                
            #son IP
            m = re.match('(  IP address: )',line)
            if m:
                neighbour_ip = line[m.end():]
                if debug: print "get remote IP",neighbour_ip
            
            #modèle
            m = re.match('Platform: ',line)
            if m:
                tmp = line[m.end():]
                neighbour_model = tmp.split(",")[0]
                if debug: print "get remote model",neighbour_model
                
            #port 
            m = re.match('(Interface: )',line)
            if m:
                if debug: print "get ports ",line
                both_ports = line
                ports= line.split(',')
                                
            if self.localName and neighbour_name and neighbour_ip and both_ports and neighbour_model:
                if debug:
                    print self.localName+","+both_ports+","+neighbour_name+","+neighbour_ip
                self.neighbourName[neighbour_name]= [neighbour_ip,both_ports,neighbour_model,ports]
                neighbour_name = ''
                neighbour_ip = ''
                both_ports =''
        
        # error at connecting
        if self.neighbourName == {}:
            if debug: print "Pas de voisins"
            raise
    
    
    
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
        #not connected,
        raise
        return
        
    neighbours = tn.read_all()
    cdpout = neighbours.splitlines()
    
    for line in cdpout:
        if debug:
            print line
        
        # Le nom du switch    local
        m = re.match(r'\w+#',line)
        if m:
            local_name = line[:m.end()-1]
                
        # Le nom du switch    remote
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
            if re.match('SEP',neighbour_name):
                # telephone on ne se connecte pas dessus
                neighbour_name = None
                continue
            if level > 0:
                if debug:
                    print level-1
                    print neighbour_ip
                    print username
                    print "calling level ",str(level-1)," for "+neighbour_ip+" "+"with username "+username+"\n"
                tnt = cisco_connect(neighbour_ip,username, password, debug)
                print_neighbours(tnt,username, password, debug,level-1)
            neighbour_name = None

    
        

        
def main():
    # Usual verifications and warnings
        
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
