#!/usr/bin/python3

import math 

class Complex:
	def __init__(self, realpart, imagpart):
		self.a = realpart
		self.b = imagpart
	def conjugate(self):
		self.b = -1*self.b
	def absolute(self):
		return math.sqrt((self.a*self.a)+(self.b*self.b))
	def argument(self):
		return math.atan2(self.b,self.a)
	def __add__(self,other):
		tmp_a = self.a + other.a
		tmp_b = self.b + other.b
		return Complex(tmp_a,tmp_b)
	def __sub__(self,other):
		tmp_a = self.a - other.a
		tmp_b = self.b - other.b
		return Complex(tmp_a,tmp_b)

z1 = Complex(2.0, -1.0)
z2 = Complex(5.0, 5.0)

print("liczba z1= "+str(z1.a) + str(z1.b)+"i")
print("moduł liczby z1= ",z1.absolute())
print("argument liczby z1= ",z1.argument(),"[rad]")
z3 = z1 + z2
print("dodawanie z1 + z2 = " + str(z3.a) +"+"+ str(z3.b) + "i")
z3 = z1 - z2
print ("odejmowanie z1 - z2 = " +str(z3.a) + str(z3.b) + "i")
z1.conjugate()
print("sprzężenie liczby z1 = " +str(z1.a) + "+" + str(z1.b) + "i")
