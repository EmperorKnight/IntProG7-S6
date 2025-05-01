# Adivinar un número

import random
import time
import os

def numero_aleatorio(numero):
    aleatorio = random.randint(1,10)
    if numero == aleatorio:
        print(f"Felicidades, adivinastes el numero")
    else:
        while numero != aleatorio:
            if numero < aleatorio:
                print(f"Introduzca un numero mayor")
            else:
                print(f"Introduzca un numero menor")
            print(f"Intente de nuevo")
            time.sleep(2)
            os.system("cls || clear")
            numero = int(input(f"Introduzca un numero \n-> "))
            if numero == aleatorio:
                print(f"Felicidades, adivinastes el numero")

def main():
    os.system("cls || clear")
    numero = int(input(f"Introduzca un numero del 1 al 10\n-> "))
    numero_aleatorio(numero)
main()
