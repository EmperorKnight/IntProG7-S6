# Promedio de calificaciones

import time
import os

def main():
    suma = 0
    promedio = 0
    contador = 0

    os.system("cls || clear")
    notas = int(input(f"Introduzca las notas del estudiante \n-> "))
    aclaracion = input(f"¿Quiere terminar el bucle?\nSi | No \n-> ")
    aclaraciones = aclaracion.capitalize()

    if aclaraciones == "Si":
        print(f"La nota final del estudiante es {notas} \nEl promedio del estudiante es {promedio}")
    else:
        while aclaraciones != "Si":
            suma += notas
            print(f"Las notas del estudiante es {suma:,}")
            time.sleep(2)
            os.system("cls || clear")
            contador += 1
            aclaracion = input(f"¿Quiere terminar el bucle? \nSi | No \n-> ")
            aclaraciones = aclaracion.capitalize()
            if aclaraciones == "Si":
                promedio = suma//contador
                print(f"La nota final del estudiante es {suma} \nEl promedio del estudiante es {promedio}")
            else:
                notas = int(input(f"Introduzca las notas del estudiante \n-> "))

main()