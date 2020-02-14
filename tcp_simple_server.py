import socket

params = ('127.0.0.1',8808)
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(params)
    s.listen(1)
    conn, addr = s.accept()
    print('Connexion acceptée: %s' % str(addr))

    with conn:
        while True:
          data = conn.recv(BUFFER_SIZE)
          if not data:
              break
          conn.send(b'Bonjour '+ data.strip()+b'.\n')

