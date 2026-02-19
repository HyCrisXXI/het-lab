from socket import *
from http.server import HTTPServer, BaseHTTPRequestHandler

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('localhost', 8000))

serverSocket.listen(1)

print("Preparado para servir...")
while True:
    connectionSocket, addr = serverSocket.accept()
    request = connectionSocket.recv(4096)
    
    for line in request:
        pass
    
    connectionSocket.sendall((header + body_response).encode())
    print(request.decode())
    
    connectionSocket.shutdown(SHUT_RDWR)
    connectionSocket.close()
