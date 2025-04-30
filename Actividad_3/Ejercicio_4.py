# Contador regresivo

import os
import time

def main():
    os.system("cls || clear")
    numero = int(input(f"Introduzca un numero \n-> "))
    while numero >= 0:
        print(f"\rConteo regresivo: {numero}  ",end = "")
        time.sleep(1)
        numero -= 1
    print(f"\nFin de la cuenta regresiva")
main()