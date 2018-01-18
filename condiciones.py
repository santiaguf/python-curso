# -*- coding: utf-8 -*-

import random
import sys
import os

edad = 21

if edad > 16 :
	print('puede manejar')
else :
	print('no puede manejar')

if edad >= 22 :
	print('tengo más de 21 ')
elif edad >= 16 :
	print('Tengo 16 y menos de 21')
else:
	print('Tengo menos de 21 años')

if ((edad >= 22) and (edad <= 22)):
	print("funciona, edad es mayor que 18 e igual a 21")
elif ((edad == 21 ) or (edad >= 23)):
	print("edad igual a 21")
elif not((edad == 30)):
	print("la edad no es igual a 30")
else: 
	print("no cumple con ninguna condición :( ")