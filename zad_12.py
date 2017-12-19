#!/usr/bin/python3

# to work on 128x128 matrix change matrix_size to 128
# console have problem with  displaying big matrixes 
from numpy import*
set_printoptions(threshold=nan)
matrix_size = 15
M1 = random.randint(1,100,(matrix_size,matrix_size))
M2 = random.randint(1,100,(matrix_size,matrix_size))
M3 = M1 + M2

print(M1)
print("\n\n")
print(M2)
print("\n\n")
print(M3)
