#!/usr/bin/python3

from numpy import*

print("Program oblicza wyznacznik macierzy")

Mx = random.randint(-10,10,(4,4))

print(Mx)
Mx_det = linalg.det(Mx)
print ("wyznacznik macierzy wynosi: ",Mx_det)

