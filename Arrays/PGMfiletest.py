##PGM Test1

import random

def mkarray():
	x = []
	for i in range(24):
		x.append(random.randint(0,20))
	return x

bigy = []









## Printing to file stuff ##
def ArrToString(arr):
	tmp1 = ""
	for i in arr:
		tmp1 += str(i) + " "
	return tmp1

def printToFile(arr):
	myf = open("test3.pgm","w")
	myf.write("P5\n100 100\n")
	for i in arr:
		myf.write(ArrToString(i))
		print(i)
	myf.close()

printToFile(bigy)
