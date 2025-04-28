# Suma de números hasta alcanzar un límite

import os

def main ():
    os.system("cls || clear")
    suma = 0
    while suma <= 100:
        os.system("cls || clear")
        numero = int(input(f"Introduzca un numero \n-> "))
        suma += numero
    print(f"Fin del Bucle. La suma total es: {suma}")
main()