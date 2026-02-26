import socket

HOST = "www.upv.es"
PORT = 80

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(5.0)
    s.connect((HOST, PORT))

    request = "GET / HTTP/1.0\r\nHost: www.upv.es\r\n\r\n"
    s.send(request.encode())

    while True:
        data = s.recv(4096)
        if not data:
            break
        print(data.decode(errors="ignore"), end="")
except socket.timeout:
    print("\nEl servidor tardo demasiado tiempo en responder")
finally:
    s.shutdown(socket.SHUT_RDWR)
    s.close()
