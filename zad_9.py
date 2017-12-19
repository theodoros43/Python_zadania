#!/usr/bin/python3

words = ['never', 'and', 'why', 'himself', 'also']
f1 = open('Zulus.txt')
input_lines = []

for line in f1:
	for word in line.split():
		if word in words:
			line = line.replace(word," ")
	input_lines.append(line)
f1.close()

f2 = open('Zulus2.txt','w+')
for line in input_lines:
	f2.write(line)
f2.close()
