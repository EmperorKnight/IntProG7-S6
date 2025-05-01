# Menú interactivo

from datetime import date
import os
import time

def menu(opciones):
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    hoy = date.today()
    if opciones == 3:
        print("Salida del programa con exito")
    else:
        while opciones != 3:
            if opciones == 1:
                print(f"Mucho gusto, humano")
            elif opciones == 2:
                mes = meses[hoy.month - 1]
                print(f"Hoy es 0{hoy.day} - {mes} - {hoy.year}")
            time.sleep(2)
            os.system("cls || clear")
            print("1 = Mostrar saludo | 2 = Mostrar fecha | 3 = Salir")
            opciones = int(input(f"Introduzca la opcion que desea realizar\n-> "))
        print("Salida del programa con exito")

def main():
    os.system("cls || clear")
    print("1 = Mostrar saludo | 2 = Mostrar fecha | 3 = Salir")
    opcion = int(input(f"Introduzca la opcion que desea realizar\n-> "))
    menu(opcion)
        
main()
            