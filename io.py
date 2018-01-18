# -*- coding: utf-8 -*-

import random
import sys
import os


#creamos el archivo
archivo = open("test.txt", "wb")
print(archivo.mode)

print(archivo.name)

archivo.write(bytes("Tengo hambre\n"))

archivo.close()

archivo = open("test.txt", "r+")

text_archivo = archivo.read()
print(text_archivo)

#eliminamos el archivo
os.remove("test.txt")