#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

target_host = "192.168.1.254"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send("GET / HTTP/1.1\r\nHost: / \r\n\r\n")
client.send("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")                                                                                                                                   
client.send("Accept-Encoding: gzip, deflate")
client.send("Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3")
client.send("Host: 192.168.1.254")
client.send("User-Agent	Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/74.0")

response = client.recv(4096)

print(response)

