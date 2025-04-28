# La tabla de multiplicar de un numero x
import os

def obtener_tabla(num):
    for i in range(1,11):
        print(f"{num:,} * {i} = {i*num:,}")

def main():
    os.system("cls || clear")
    numero = int(input(f"Dime un numero: \n-> "))
    obtener_tabla(numero)

main()