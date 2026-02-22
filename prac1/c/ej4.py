from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('localhost', 8000))

serverSocket.listen(1)


sock_name = serverSocket.getsockname()
base_url = str(sock_name[0]) + ":" + str(sock_name[1])

print("Sirviendo en:", base_url)
while True:
    connectionSocket, addr = serverSocket.accept()
    request = b""

    while True:
        data = connectionSocket.recv(4096)
        if not data:
            break
        request += data

        if b"\r\n\r\n" in request:
            break

    request_str = request.decode()

    url = request_str.split("GET ", 1)[1].split()[0]
    print (request_str)
    for line in request_str.split('\n'):
        if "User-Agent: " in line:
            browser = line.split("User-Agent: ", 1)[1]
            break

    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hola Mundo</h1>" \
    "<b>La dirección URL pedida es: " + base_url + url + "<br>Su buscador es: " + browser + "</b>"

    connectionSocket.send(response.encode(encoding="ISO-8859-1"))

    connectionSocket.shutdown(SHUT_RDWR)
    connectionSocket.close()
