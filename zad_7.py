#!/usr/bin/python3

import math

print("program oblicza pierwiastki równania kwadratowego")
a = float(input("podaj a: "))
b = float(input("podaj b: "))
c = float(input("podaj c: "))

delta = b*b - 4*a*c
if (delta > 0):
	x1=((-1*b)+math.sqrt(delta))/(2*a)
	x2=((-1*b)-math.sqrt(delta))/(2*a)
	print("równanie posiada dwa pierwiastki:\n")
	print("x1 = ",x1, " x2 = ",x2)
elif (delta == 0):
	x0= (-1*b)/(2*a)
	print("równanie posiada jeden pierwiastek:\n")
	print("x0 = ",x0)
else:
	delta = -1* delta
	tmp1 = -1*math.sqrt(delta)/(2*a)
	tmp2 =    math.sqrt(delta)/(2*a)
	if(tmp1 >= 0):
		x1=str((-1*b)/(2*a)) + "+" + str(tmp1) + "i"
	else:
		x1=str((-1*b)/(2*a)) + str(tmp1) + "i"
	if(tmp2 >= 0):
		x2=str((-1*b)/(2*a)) + "+" +  str(tmp2) + "i"
	else:
		X2=str((-1*b)/(2*a)) + str(tmp2) + "i"
	print("delta ujemna")
	print("równanie posiada dwa pierwiastki zespolone:\n")
	print("x1 = ",x1, " x2 = ",x2)

