# ACTIVIDAD 05
# Ejemplos de parametros por consola y "sobrecarga" con *args en Python 3.

import sys

# 1) Pasar varios parametros desde consola.
# Uso: python Actividad5.py 3 5 7
if len(sys.argv) > 1:
    print("parametros consola:", sys.argv[1:])
    numeros = [int(x) for x in sys.argv[1:]]
    print("suma consola:", sum(numeros))
else:
    print("sin parametros consola")


# 2) "Sobrecarga" con distintos numeros de parametros.
# En Python se hace con valores por defecto y *args.

def sumar_dos(a, b=0):
    return a + b


def sumar_varios(*numeros):
    # *numeros acepta cualquier cantidad de argumentos (incluido ninguno)
    return sum(numeros)


print("sumar_dos(4, 6):", sumar_dos(4, 6))
print("sumar_dos(4):", sumar_dos(4))
print("sumar_varios(1, 2, 3):", sumar_varios(1, 2, 3))
print("sumar_varios():", sumar_varios())