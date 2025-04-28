#  Contador regresivo

import os

def main():
    os.system("cls || clear")
    numero = int(input(f"Introduzca un numero \n-> "))
    i = numero
    while i != 0:
        i -= 1
        print(f"Cuenta regresiva: {i}")

main()