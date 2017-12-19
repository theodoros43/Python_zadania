#!/usr/bin/python3

import threading
import time

#The philosopher thread
def philosopher(left,right):
	count = 0
	while True:
		print(count)
		count = count+1
		with left:
			#time.sleep(0.1)
			with right:
				time.sleep(1)
				print (str(threading.currentThread()) + "eating")
							
# The chopsticks
NSTICKS = 5
chopsticks = [threading.Lock() for n in range(NSTICKS)]
#Create all of the philosophers
phils = [threading.Thread(target=philosopher, args=(chopsticks[n],chopsticks[(n+1)% NSTICKS])) for n in range(NSTICKS)]
#Run all of the philosophers
for p in phils:
	p.start()
