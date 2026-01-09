# ACTIVIDAD 05
# Ejemplos de parametros por consola y "sobrecarga" con *args en Python 3.

import sys

# 1) Pasar varios parametros desde consola.

print("Nombre:", sys.argv[1])
print("Edad:", sys.argv[2])


# 2) "Sobrecarga" con distintos numeros de parametros.
# En Python se hace con valores por defecto y *args.

def sumar_dos(a, b=0):  # Suma dos numeros, el segundo es opcional
    return a + b

def suma(*numeros):  # Suma cualquier cantidad de numeros
    total = 0
    for n in numeros:
        total += n
    return total

print(suma(2, 3)) # Suma de dos numeros
print(suma(5, 10, 15)) # Suma de tres numeros
print(suma(1, 2, 3, 4, 5)) # Suma de cinco numeros




