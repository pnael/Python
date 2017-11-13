import socket

params = ('127.0.0.1',8808)
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"World",params)
data , _=s.recvfrom(BUFFER_SIZE)
print("\t Donnée récupérée du serveur : %s" % data)
s.close()

