# Número de dígitos

import os

def contar_digitos(digito):
    conteo_digitos = 0
    while digito > 0:
        digito = digito // 10
        conteo_digitos += 1
    print("La cantidad de digitos del numero es: ",conteo_digitos)    

def main():
    os.system("cls || clear")
    numero = int(input(f"Introduzca un numero positivo\n-> "))
    contar_digitos(numero)

main()