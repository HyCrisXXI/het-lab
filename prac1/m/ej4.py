import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 9000))

s.listen(1)


client, addr = s.accept()

request = client.recv(2048).decode()

if request:
    lines = request.splitlines()

    first_line = lines[0].split(" ")
    url = first_line[1]

    user_agent = ""
    for line in lines:
        if line.startswith("User-Agent:"):
            user_agent = line.split(" ")[1]
    
    cuerpo = f"Hola! Has pedido la URL: {url}\n"
    cuerpo += f"Tu navegador es: {user_agent}\n"
    
    respuesta = "HTTP/1.1 200 OK\r\n"
    respuesta += "\r\n"
    respuesta += cuerpo
    
    client.send(respuesta.encode())

client.close()
s.close()