import socket

host = "www.upv.es"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

request = "GET / HTTP/1.0\r\nHost: www.upv.es\r\n\r\n"
s.send(request.encode())

while True:
    data = s.recv(4096)
    if not data:
        break
    print(data.decode(errors="ignore"), end="")

s.close()
