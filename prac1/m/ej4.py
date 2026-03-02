import socket

HOST = '127.0.0.1'
PORT = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Servidor en http://{HOST}:{PORT}")

    while True:
        client, addr = s.accept()

        request = client.recv(2048).decode(errors="ignore")
        
        if request:
            lines = request.splitlines()
            if len(lines) > 0:
                first_line = lines[0].split()
                url = first_line[1] if len(first_line) > 1 else "/"

                user_agent = ""
                for line in lines:
                    if line.lower().startswith("user-agent:"):
                        user_agent = line.split(":", 1)[1].strip()
                
                cuerpo = f"Hola! Has pedido la URL: http://{HOST}:{PORT}{url}\n"
                cuerpo += f"Tu navegador es: {user_agent}\n"
                

                respuesta = "HTTP/1.1 200 OK\r\n"
                respuesta += "Content-Type: text/plain; charset=utf-8\r\n"
                respuesta += f"Content-Length: {len(cuerpo.encode())}\r\n"
                respuesta += "\r\n"
                respuesta += cuerpo
                
                client.sendall(respuesta.encode())
        
        client.close()

except KeyboardInterrupt:
    print("\nFin del servidor")
finally:
    s.close()