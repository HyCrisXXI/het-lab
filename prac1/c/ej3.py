import socket
import sys

s: socket = None
host_name: str = 'www.upv.es'
port: int = 80
    
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("la creación del socket fallo con error: %s" %(err))
    sys.exit()

s.settimeout(5)

try:
    host_ip = socket.gethostbyname(host_name)
except socket.gaierror:
    print("hubo un error al resolver el host")
    sys.exit()

s.connect((host_ip, port))

print("el socket se conectó correctamente a la UPV")

request = b"GET / HTTP/1.1\r\nHost: " + host_ip.encode() + b"\r\n\r\n"

s.sendall(request)

response = b""
while True:
    try:
        data = s.recv(4096)
        if not data:
            break
        response += data
    except socket.timeout:
        print("Error: han pasado más de 5 segundos sin respuesta del servidor")
        break

s.shutdown(socket.SHUT_RDWR)
s.close()

print("conexión con la UPV finalizada")
print("resultado:\n", response.decode(encoding="utf-8"))