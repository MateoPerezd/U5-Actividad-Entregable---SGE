# ACTIVIDAD 06
# Lista de [altura, peso] y ordenacion con key functions.

# Cada elemento es una lista con dos valores: altura y peso.
personas = [
    [170, 70],
    [180, 75],
    [180, 68],
    [165, 80],
    [175, 72],
    [170, 65],
]

# La "key function" es una funcion (o cualquier callable) que recibe un solo
# argumento y devuelve el valor que se usa para ordenar. Se llama una sola vez
# por cada elemento, por eso es eficiente.
# Orden: mayor altura (desc) y, en caso de empate, menor peso (asc).
personas_ordenadas = sorted(personas, key=lambda p: (-p[0], p[1]))

print("original:", personas)
print("ordenadas:", personas_ordenadas)