from sys import argv

if len(argv) > 1:
    nombre_fichero = argv[1]
    try:
        with open(nombre_fichero, 'r') as fd:
            lines= fd.readlines()
            for line in lines:
                print(line, end='')

    except IOError as error:
        print("No existe " + nombre_fichero + ".")
else:
    print("Dar un nombre de fichero como argumento al ejecutar el programa.")