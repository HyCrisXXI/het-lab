import sys

class PythonBasics:
    
    @staticmethod
    def tipos() -> None:
        lista = [2,3,2,9,5,3,2,4,1]
        tupla = (1,2,3,4,6,5)
        conjunto = set([1,2,3,4,4,4])
        diccionario = {'a':1, 'b':2, 'c':3}
        entero = 12
        double = 12.2
        doubleplus = 12.2223434
        string = "hola mundo"
        boolean = True
        binario = 0b10101
        octal = 0o231312321
        hexadecimal = 0x231231
        complejo = 2+3j
        print(f'Numero complejo: {complejo}, parte real = {complejo.real}, parte imaginaria: {complejo.imag}')
        sumadi = double + complejo
        print(f'Suma double y complejo = {sumadi}')
        print(f'{doubleplus:.2f}')
        print(f'Esto es una lista: {lista}, esto una tupla: {tupla}, esto un conjunto: {conjunto} y esto un diccionario: {diccionario}')
        print(f'Es {complejo} un número complejo? {isinstance(complejo, complex)}')
        print(f'Esto es un número binario: {binario}, esto una octal: {octal}, y esto un hexadecimal: {hexadecimal}')
    
    @staticmethod
    def is_par(a: int) -> bool:
        try:
            num = int(a)
            return True if (num % 2) == 0 else False
        except:
            print("Introduzca un número válido")
    
    @staticmethod
    def list_sum(l: list) -> int:
        try:
            sum = 0
            for elem in l:
                sum += int(elem)
            return sum
        except(TypeError):
                print("Introduzca una lista válida")
    
    @staticmethod
    def main(): 
        print("Escribe un número a continuación para saber si es o no par")
        es_par = None
        while es_par == None:
            num = input()
            es_par = PythonBasics.is_par(num)
        print(f'El número {num} es {"par" if es_par else "impar"}')

        print("A continuación se ofrece información poco relevante:\n")
        PythonBasics.tipos()


class IOUsage:
    @staticmethod
    def main():
        print("Introduzca a continuación el nombre del archivo a leer")
        try:
            file_name: str = input()
            with open(file_name, 'r', encoding="UTF-8") as f:
                print(f.read())
        except IOError as error:
            print(f'No existe ningún archivo con el nombre {file_name},', error)
        except UnicodeDecodeError as error2:
            print("Hubo un error leyendo el archivo", error2)


if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("Uso: py prac1.py [basics|io]")
    else:
        opcion = sys.argv[1].lower()
        match opcion:
            case 'basics':
                PythonBasics.main() 
            case 'io':
                IOUsage.main()
            case _:
                print('Introduzca una opción válida (basics | io)')