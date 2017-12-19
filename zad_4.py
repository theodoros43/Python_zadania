#!/usr/bin/python3

import random
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Lock, Array
import matplotlib
import numpy as np
matplotlib.use('Agg')
import matplotlib.pyplot as plt 

# function calculating histogram values
def histogram(list, bars):
	for i in list:
		bars[i] = bars[i] + i
	return bars

# create list of 100 elements (simple to devide by 4)
list = []
for l in range(0,100):
	list.append(random.randint(0,59)) # there will be 60 bars
# create 60 empty bars to store data in shared memory
bars = Array('i', range(60))
for l in range(0,60):
	bars[l] = 0

bars1 = [0]*60
# define processes for multiprocessing operation
p1 = Process(target=histogram, args=(list[0:25], bars))
p2 = Process(target=histogram, args=(list[25:50], bars))
p3 = Process(target=histogram, args=(list[50:75], bars))
p4 = Process(target=histogram, args=(list[75:100], bars))

# execute processes
p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

histogram(list, bars1)
# create output file
plt.hist(bars, bins = 60)
plt.hist(bars1,bins = 60)
plt.savefig('histogram.png')
