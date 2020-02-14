import socketserver
import threading

params = ('127.0.0.1',8808)

class ExampleUDPHandler(socketserver.DatagramRequestHandler):
    def handle(self):
        cur_thread = threading.current_thread()
        data = self.rfile.readline().strip()
        print('>>> Reçu: %s',data,', current_thread:',cur_thread)
        self.wfile.write(b"Bonjour " + data.strip()+ b".\n")

class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass

if __name__ == '__main__':
    server = socketserver.UDPServer(params, ExampleUDPHandler)
    server.thread = threading.Thread(target=server.serve_forever())
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:",server_thread.name)
    input()
    server.shutdown()
    server.server_close()


