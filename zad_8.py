#!/usr/bin/python3

import random
list = []
list_length = 50
print("przed sortowaniem:")
for i in range(list_length):
	list.append(int(random.randint(1,100)))
	print(list[i], end=' ')
for j in range(list_length-1):
	for i in range(list_length-1):
		if (list[i] < list[i+1]):
			tmp = list[i]
			list[i] = list[i+1]
			list[i+1] = tmp
print("\npo sortowaniu: ")
for i in range(50):
	print(list[i], end=' ')
print()
