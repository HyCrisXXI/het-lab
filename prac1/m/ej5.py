import base64

try:
    with open("hosts_b64.txt", "r") as f:
        contenido_encoded = f.read()
    
    contenido_decoded = base64.b64decode(contenido_encoded)
    
    print(contenido_decoded.decode('utf-8'))

    with open("hosts_decoded.txt", "w") as decoded_file:
        decoded_file.write(contenido_decoded)

    
except IOError:
    print("Error: El archivo hosts_b64.txt no existe.")