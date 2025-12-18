from crear_cuenta import proceso_de_cuenta_nueva
from logueo import logueo_usuario
from os import system

while True:
    system("cls")
    print("Por favor, digite uno de los números para ejecutar el proceso:\n1. Crear cuenta\n2. Logueo")
    select=input('Digite el numero: ')
    while True:
        if select == '1':
            system("cls")
            proceso_de_cuenta_nueva()
            break
        elif select == '2':
            system("cls")
            logueo_usuario()
            break
        else:
            print("Selección no válida. Por favor, elija 1 o 2.")
            input('Digite enter para continuar')
            system("cls")