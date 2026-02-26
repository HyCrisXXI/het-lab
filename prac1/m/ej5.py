import base64
import sys

if(len(sys.argv) < 2):
    sys.exit("Uso: ej5.py <archivo codificado> [<archivo salida>]")

input_file = sys.argv[1]

output_file = sys.argv[2] if len(sys.argv) > 2 else input_file + ".decoded"

try:
    with open(input_file, "r") as encoded_file:
        encoded_content = encoded_file.read()
    
    decoded_content = base64.b64decode(encoded_content)

    with open(output_file, "wb") as decoded_file:
        decoded_file.write(decoded_content)
    
except IOError:
    sys.exit(f"Error: El archivo {input_file} no existe.")
