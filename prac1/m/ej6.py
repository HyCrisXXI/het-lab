import struct
import sys

if len(sys.argv) != 2:
    sys.exit("Uso: python3 ej6.py <numero>")

try:
    num = int(sys.argv[1])
except ValueError:
    sys.exit("El argumento debe ser un número entero")

    b1 = struct.pack('<B', num & 0xFF)
    b2 = struct.pack('<H', num & 0xFFFF)
    b4 = struct.pack('<I', num & 0xFFFFFFFF)

sys.stdout.buffer.write(b1)
sys.stdout.buffer.write(b2)
sys.stdout.buffer.write(b4)
