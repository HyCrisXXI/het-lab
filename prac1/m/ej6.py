import struct
import sys

if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("El argumento debe ser un número entero.")
        sys.exit(1)
    print(f"Número {num}")
    
    try:   
        print(f"1 byte:  {struct.pack('<b', num)}")
    except struct.error as e:
        print(f"Error: {e}")
    try:   
        print(f"2 bytes: {struct.pack('<h', num)}")
    except struct.error as e:
        print(f"Error: {e}")
    try:   
        print(f"4 bytes: {struct.pack('<i', num)}")
    except struct.error as e:
        print(f"Error: {e}")

else:
    print("Dar un número como argumento al ejecutar el programa.")