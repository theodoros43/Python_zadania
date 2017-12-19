#!/usr/bin/python3

from numpy import *
set_printoptions(threshold=nan)
matrix_size = 8
M1 = random.randint(1,10,(matrix_size,matrix_size))
M2 = random.randint(1,10,(matrix_size,matrix_size))
M3 = dot(M1,M2)
print(M1)
print()
print(M2)
print()
print(M3)
