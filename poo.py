# -*- coding: utf-8 -*-

import random
import sys
import os

class Animales :
	__name = ""
	__height = 0
	__width = 0
	__sound = 0



	#constructor, más barato, imposible
	def __init__(self,name,height,width,sound):
		self.__name = name
		self.__height = height
		self.__width = width
		self.__sound = sound

	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_height(self, height):
		self.__height = height

	def get_height(self):
		return self.__height

	def set_width(self, width):
		self.__width = width

	def get_width(self):
		return self.__width
	
	def set_sound(self, sound):
		self.__sound = sound

	def get_sound(self):
		return self.__sound

	def get_type(self):
		print("Animal")

	def toString(self):
		return "El {} mide {} y mide {} y suena {}.".format(self.__name, self.__height, self.__width, self.__sound)

	gato = Animales("gato",33,30,"miau")
	print(gato.toString())	