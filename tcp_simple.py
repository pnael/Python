import socket

params = ('127.0.0.1',8808)
BUFFER_SIZE = 1024

s = socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(params)
s.listen(1)
