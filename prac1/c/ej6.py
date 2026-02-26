import struct
import sys

if(len(sys.argv) < 2):
    print("Uso: python3 e6.py <numero>")

num = int(sys.argv[1])

try:
    b1 = struct.pack("<B", num)
    b2 = struct.pack("<H", num)
    b4 = struct.pack("<I", num)
except struct.error:
    print("Introduzca un número en el rango [0, 255]")
    sys.exit()
sys.stdout.buffer.write(b1 + b2 + b4)
