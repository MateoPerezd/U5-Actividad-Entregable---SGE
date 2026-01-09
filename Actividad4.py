# ACTIVIDAD 04

# 1) Operador "is": compara identidad (mismo objeto en memoria).
a = [1, 2, 3]
b = [1, 2, 3]
c = a


print( a is b)   # "a" y "b" son diferentes objetos, dará resultado False
print( a is c)   # "c" apunta al mismo objeto que "a", son idénticos, dará resultado True


# 2) Operador "not": niega una condicion booleana.

print(not (a is b))  # Negación de la comparación anterior, dará True

# Otro ejemplo.

print( not (5 > 3)) # Negación de True es False
print( not (2 + 2 == 5)) # Negación de False es True


# 3) Operador "in": comprueba pertenencia en secuencias o colecciones.

print (2 in a)  # 2 está en la lista "a", dará True
print (8 in b)  # 8 no está en la lista "b", dará False

# Otro ejemplo con cadenas.

frase = "Me gusta Python"
print("Python" in frase)  # La palabra está en la frase, dará True