# ACTIVIDAD 03

# Ejemplo de almacenamiento de usuario y contrasena con hash usando lista y diccionario.

import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


# 1) Utilizando una lista (lista de tuplas: (usuario, hash)).
usuarios_lista = []

usuarios_lista.append(("miguel", hash_password("clave123"))) 
usuarios_lista.append(("alejandro", hash_password("alejandro2026")))
usuarios_lista.append(("sara", hash_password("contraseña123")))
usuarios_lista.append(("carlos", hash_password("nolavasaadivinar")))
usuarios_lista.append(("nuria", hash_password("abc123")))

# Consulta 1 en lista: buscar el hash del usuario miguel.

consulta_usuario = "miguel"

for usuario, password in usuarios_lista:
    if usuario == consulta_usuario:
        print("Usuario encontrado:", usuario, "\nHash:", password)
        break

# Otro tipo de consulta

# Consulta 2 en lista:  Mostrar el tercer usuario almacenado

print(usuarios_lista[2])


# 2) Utilizando un diccionario.

usuarios_dic = {
    "miguel": hash_password("clave123"),
    "alejandro": hash_password("alejandro2026"),
    "sara": hash_password("contraseña123"),
    "carlos": hash_password("nolavasaadivinar"),
    "nuria": hash_password("abc123"),
}

# Consulta 1 en diccionario: obtener el hash de carlos.

consulta_usuario_dic = "carlos"
print("usuario:", consulta_usuario_dic, 
      "\nhash:", usuarios_dic.get(consulta_usuario_dic))


# Consulta 2 en diccionario: verificar si una contraseña coincide.

usuario_verif_dic = "nuria"
password_verif_dic = "abc123"
hash_verif_dic = hash_password(password_verif_dic)
print("verificación:", usuario_verif_dic, "\ncoincide:", usuarios_dic.get(usuario_verif_dic) == hash_verif_dic)