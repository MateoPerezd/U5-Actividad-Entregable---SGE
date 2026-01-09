# ACTIVIDAD 01

import copy

# 1) Clonar una lista y diferenciar entre shallow copy y deep copy.

listado = [1, 2, 3, [4, 5], 6 , 7, 8]

# Shallow copy: copia la lista, pero las listas internas siguen siendo las mismas referencias.
listadoConShallow = listado.copy()  


# Deep copy: copia toda la estructura, incluidas listas internas.
listadoConDeep = copy.deepcopy(listado)


# Diferencia:
# Shallow copy copia la lista, pero NO los objetos internos
# Deep copy copia todo recursivamente



# 2) Agregar un elemento a una lista.

listado.append(9)

# listado ahora sería[1, 2, 3, [4, 5], 6 , 7, 8, 9]


# 3) Quitar un elemento de una lista.

listado.remove(3)  

# listado ahora sería [1, 2, [4, 5], 6 , 7, 8, 9]


# 4) Crear una lista nueva con los 4 ultimos elementos.

ultimos_4 = listado[-4:]

# ultimos_4 sería [6, 7, 8, 9]


# 5) Convertir las palabras de una cadena a una lista.

cadena = "Hola mundo de Python, estamos en SGE"
listado_palabras = cadena.split()  

# listado_palabras sería ['Hola', 'mundo', 'de', 'Python,', 'estamos', 'en', 'SGE']



# 6) Comentarios de una linea.
# Este es un comentario de una linea.

# 7) Comentarios multilinea.
"""
Este es un comentario multilinea.
Se puede usar para explicar bloques grandes.
"""