# -*- coding: utf-8 -*-

import random
import sys
import os

print("hola men")

#3 comentario que no sirve pa nada
name = "santo"
print(name)

print("1+2-3*2 =", 1+2-3*2)

print((100+200)*3)
print(25/5+5*3)
print((5+5)/(5-3))
print(50-44*1+7)

variable = "pepito perez"
variable_larga = ''' hola 
mundo '''

print(variable_larga)

#4 Strings dentro de otro string
saludo = "hola %s y como va todo %s "
p1 = "santi"
p2 = "eli"
print(saludo %(p1,p2))

jugadores = ["messi", "cristiano", "neymar", "dybala"]
print("jugador " + jugadores[0])

#imprimir todos los elementos del vector o lista
print(jugadores[0:3])

#5 vector o lista
lista_tareas = ["lavar", "planchar", "jugar", "reir"]

#matriz
lista_cosas = [lista_tareas, jugadores]

print(lista_cosas[1][2])

lista_tareas.append("viajar")
print(lista_cosas)

#total de elementos
print(len(lista_cosas))
print(max(lista_cosas))
print(min(lista_cosas))


#6 tuplas
tuple = (1,2,3,4,5,6,7,8,9,0)
print(tuple)
print(tuple[3])

nuevo_tuple = list(tuple)
#nueva_lista2 = tuple(nuevo_tuple)

#len(tuple)

#7 diccionarios o mapas
paises = {'Colombia' : 'Bogotá', 
	'Argentina' : 'Buenos Aires',
	'México' : 'Cuidad de México',
	'Chile' : 'Santiago de Chile',
	'Ecuador' : 'Quito' 
	}
print(paises['Chile'])

print(paises)

# paises['Colombia'] = 'Capital'

print(len(paises))
print(paises.get('Argentina'))

print(paises.keys())
print(paises.values())