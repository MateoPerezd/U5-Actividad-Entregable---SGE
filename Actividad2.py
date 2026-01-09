# ACTIVIDAD 02

# 1) Recibe 2 numeros y devuelve la suma.

def sumar(a, b):
    return a + b


# 2) Recibe una lista y la modifica en la misma referencia.

#    Dobla los valores de todos los elementos. No devuelve nada.
def doblar_lista(lista):
    for i in range(len(lista)):
        lista[i] *= 2


# 3) Recibe una lista y devuelve una copia con los valores doblados.
#    La lista original no se modifica.
def doblar_copia(lista):
    copia = lista.copy()  # shallow copy suficiente para lista de numeros
    for i in range(len(copia)):
        copia[i] *= 2
    return copia

