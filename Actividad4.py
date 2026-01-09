# ACTIVIDAD 04
# Ejemplos de los operadores is, not e in en Python 3.

# 1) Operador "is": compara identidad (mismo objeto en memoria).
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a == b:", a == b)   # mismo contenido
print("a is b:", a is b)   # no son el mismo objeto
print("a is c:", a is c)   # c apunta al mismo objeto que a

# 2) Operador "not": niega una condicion booleana.
activo = False
print("not activo:", not activo)
print("not (5 > 3):", not (5 > 3))

# 3) Operador "in": comprueba pertenencia en secuencias o colecciones.
lista = [10, 20, 30]
texto = "hola mundo"

print("20 in lista:", 20 in lista)
print("50 in lista:", 50 in lista)
print("'mundo' in texto:", "mundo" in texto)
print("'python' in texto:", "python" in texto)

# Ejemplo combinado: usar not in.
print("40 not in lista:", 40 not in lista)