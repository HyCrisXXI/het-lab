import socketserver
import socket
import http.server
import sys

IP = "127.0.0.1"
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((IP, PORT), Handler) as httpd:
    print("sirviendo como puerto", PORT)

respones = b"User-Agent:"

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("finalizando conexión...")
    sys.exit()