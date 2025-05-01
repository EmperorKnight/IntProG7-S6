# Contador regresivo

import os
import time

def cuenta_regresiva(tiempo):
    for i in range(tiempo,0,-1):
        print(f"\rConteo regresivo: {i}  ",end = "")
        time.sleep(1)
    print(f"\nFin de la cuenta regresiva")

def main():
    os.system("cls || clear")
    numero = int(input(f"Introduzca un numero \n-> "))
    cuenta_regresiva(numero)
main()