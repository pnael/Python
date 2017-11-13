import socket

params = ('127.0.0.1',8808)
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(params)
s.send(b"World")
data=s.recv(BUFFER_SIZE)
print("\t Donnée récupérée du serveur : %s" % data)
s.close()

