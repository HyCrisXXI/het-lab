import struct
import sys

if(len(sys.argv) < 2):
    print("Uso: python3 e6.py <numero>")

try:
    num = int(sys.argv[1], 0)

    b4 = struct.pack("<I", num)
    sys.stdout.buffer.write(b4)

except Exception as e:
    sys.stderr.write(f"Error: {e}\n")

