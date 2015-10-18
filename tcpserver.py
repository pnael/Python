#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9998

#Start server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)


#Client thread
def handle_client(client_socket):
    req = client_socket.recv(1024)
    print "[*] received %s" % req
    #send back a packet
    client_socket.send("ACK!")
    client_socket.close()

while True:

    client,addr = server.accept()

    print "[*] Accepted connection from: %s:%d" %(addr[0],addr[1])
    #Start a Thread
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
