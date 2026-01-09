# ACTIVIDAD 07
# Clase Car con matricula y color, mas metodos adicionales y creacion de n instancias.

import random


class Car:
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def imprimir(self):
        print("matricula:", self.matricula, "color:", self.color)

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color

    def es_color(self, color_consulta):
        return self.color == color_consulta


colores = ["red", "white", "black", "pink", "blue"]

n = int(input("Introduce n: "))

coches = []
for i in range(1, n + 1):
    color = random.choice(colores)
    coche = Car(i, color)
    coches.append(coche)

limite = 10 if n >= 10 else n
for i in range(limite):
    coches[i].imprimir()