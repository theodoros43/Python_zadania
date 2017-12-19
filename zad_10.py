#!/usr/bin/python3

dictionary = {'never':'almost never', 'and':'also', 'also':'and'}
f1 = open('ZygoteBody.txt')
input_lines = []
for line in f1:
	for word in line.split():
		if word in dictionary:
			line = line.replace(word,dictionary[word])
	input_lines.append(line)
f1.close()

f2 = open('ZygoteBody2.txt','w+')
for line in input_lines:
	f2.write(line)
f2.close()
