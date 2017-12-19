#!/usr/bin/python3

f = open('zad_1_plik', 'w')
f.write('Hello\n')
f.write('darkness\nmy\nold\nfriend')
f.close()

f = open('zad_1_plik', 'r')
try:
	text = f.read()
finally:
	f.close()
print(text)
