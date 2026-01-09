# ACTIVIDAD 03
# Ejemplo de almacenamiento de usuario y contrasena con hash usando lista y diccionario.

import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


# 1) Utilizando una lista (lista de tuplas: (usuario, hash)).
usuarios_lista = []

usuarios_lista.append(("miguel", hash_password("clave123")))
usuarios_lista.append(("alejanro", hash_password("alejandro2026")))
usuarios_lista.append(("sara", hash_password("contraseña123")))
usuarios_lista.append(("carlos", hash_password("nolavasaadivinar")))
usuarios_lista.append(("nuria", hash_password("abc123")))

# Consulta 1 en lista: buscar el hash del usuario "marta".
consulta_usuario = "marta"
resultado_hash = None
for usuario, h in usuarios_lista:
    if usuario == consulta_usuario:
        resultado_hash = h
        break
print("lista -> usuario:", consulta_usuario, "hash:", resultado_hash)

# Mostrar el primer usuario almacenado
print(usuarios_lista[0])

# Consulta 2 en lista: verificar si una contrasena coincide.
usuario_verif = "sara"
password_verif = "contraseña123"
hash_verif = hash_password(password_verif)
coincide = False
for usuario, h in usuarios_lista:
    if usuario == usuario_verif and h == hash_verif:
        coincide = True
        break
print("lista -> valida:", usuario_verif, coincide)

# Mostrar el tercer usuario almacenado
print(usuarios_lista[2])


# 2) Utilizando un diccionario (usuario -> hash).

usuarios_dic = {
    "miguel": hash_password("clave123"),
    "alejandro": hash_password("alejandro2026"),
    "sara": hash_password("contraseña123"),
    "carlos": hash_password("nolavasaadivinar"),
    "nuria": hash_password("abc123"),
}

# Consulta 1 en diccionario: obtener el hash de "carlos".
consulta_usuario_dic = "carlos"
print("diccionario -> usuario:", consulta_usuario_dic, "hash:", usuarios_dic.get(consulta_usuario_dic))

# Consulta 2 en diccionario: verificar si una contrasena coincide.
usuario_verif_dic = "ana"
password_verif_dic = "clave123"
hash_verif_dic = hash_password(password_verif_dic)
print("diccionario -> valida:", usuario_verif_dic, usuarios_dic.get(usuario_verif_dic) == hash_verif_dic)