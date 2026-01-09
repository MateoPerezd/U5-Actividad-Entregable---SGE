# ACTIVIDAD 07

import random


class Car:

    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def imprimir(self):
        print("matricula:", self.matricula,
               "\ncolor:", self.color)

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color

    def es_color(self, color_consulta):  # Devuelve True si el color coincide
        return self.color == color_consulta


colores = ["red", "white", "black", "pink", "blue"]

n = int(input("Introduce número de coches: "))

coches = []

for i in range(1, n + 1): # Crear n coches
    color = random.choice(colores) # Color aleatorio
    coche = Car(i, color) # Matrícula es el número i
    coches.append(coche)

for coche in coches[:10]: # Imprimir los primeros 10 coches
    coche.imprimir() 