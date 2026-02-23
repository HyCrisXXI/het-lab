import struct
import sys

def main():
	print('Escribe un número válido')
	num:int = 0
	try:
		num = int(input())
	except ValueError:
		print('Por favor, introduzca un número válido')
		sys.exit()
	try:
		byte1 = struct.pack('<b',num)
		byte2 = struct.pack('<h',num)
		byte4 = struct.pack('<i',num)

		sys.stdout.buffer.write(byte1)
		sys.stdout.buffer.write(byte2)
		sys.stdout.buffer.write(byte4)
  
		print(byte1 + "/n" + byte2 +"/n" + byte4)
	except struct.error as e:
		print(f'Error de empaquetado: {e}. (El número es muy grande)')

if __name__ == '__main__':
	main()
