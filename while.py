# -*- coding: utf-8 -*-

import random
import sys
import os

randon_number = random.randrange(0,10)

print("soy el ", randon_number)

while(randon_number != 8):
	print(randon_number)
	randon_number = random.randrange(0,10)

print(randon_number)

print('\n')

i = 0;

while (i <= 20):
	i += 1
	if (i%2 == 0):
		print(i)
