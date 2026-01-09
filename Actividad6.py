# ACTIVIDAD 06

# Lista de [altura, peso] y ordenacion con key functions.

# Cada elemento es una lista con dos valores: altura y peso.
personas = [
    [170, 71],
    [180, 75],
    [183, 67],
    [165, 80],
    [174, 72],
    [170, 65],
]

# Orden: mayor altura (desc) y, en caso de empate, menor peso (asc).

personas.sort(key=lambda x: (-x[0], x[1])) # Ordena por altura descendente y peso ascendente

print(personas)
