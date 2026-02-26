import struct
import sys

if len(sys.argv) < 2:
    sys.exit("Uso: python3 ej6.py <numero>")

try:
    num = int(sys.argv[1])
except ValueError:
    sys.exit("El argumento debe ser un número entero")
    
try:   
    b1 = struct.pack('<B', num)
    b2 = struct.pack('<H', num)   
    b4 = struct.pack('<i', num)
except struct.error as e:
    sys.exit(f"Error: {e}")

sys.stdout.buffer.write(b1 + b2 + b4)
