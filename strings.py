# -*- coding: utf-8 -*-

import random
import sys
import os

#print('cómo te llamas?')
#nombre = sys.stdin.readLine()
nombre = raw_input('cómo te llamas?')
print('\n')
print "Hola,", nombre

string_largo = "    no puede llover todos los días"

print(string_largo[0:4])
print(string_largo[-5:])
print(string_largo[:-5])

print(string_largo[:4]+' o sí?')

print("la %c es la inicial de %s y el %d es parte de %.3f" % ('C','Catalina', 100, 1.1))

print(string_largo.find('llover'))

print(string_largo.isalpha())

print(string_largo.isalnum())

print(len(string_largo))

print(string_largo.replace('no','si'))

print(string_largo.strip())

lista = string_largo.split(" ")
print(lista)