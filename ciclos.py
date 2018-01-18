# -*- coding: utf-8 -*-

import random
import sys
import os

for loop in range(0,10):
	print(loop)


print('\n')

lista_mercado = ['jugo','fruta','carne','pollo']
for loop_list in lista_mercado:
	print(loop_list)

print('\n')

for lista_numeros in [2,4,6,8,10]:
	print(lista_numeros)

print('\n')

listas = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
	for y in range(0,3):
		print(listas[x][y])