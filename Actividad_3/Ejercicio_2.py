# Contar números pares hasta un límite

import os

def numeros_pares(num):
    contador = 0
    while contador < num:
        par = contador % 2
        if par == 0:
            print(f"El numero {contador} es par")
        else:
            print("El numero {} es inpar".format(contador))
        contador += 1


def main():
    os.system("cls || clear")
    numero = int(input(f"Introduzca un numero \n-> "))
    numeros_pares(numero)

main()