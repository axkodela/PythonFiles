import random

def mkArray():
	x = []
	for n in range(100):
		x.append(random.randint(0,1))
	return x

bigy = []
for i in range(100):
	bigy.append(mkArray())

numOfRows = 0
numOfCols = 0

for m in bigy:
	numOfRows+=1
	for o in m:
		numOfCols+=1

print("Num Of Rows = " + str(numOfRows) + "\nNum Of Cols = " + str(numOfCols))

def ArrToString(arr):
	tmp1 = ""
	for i in arr:
		tmp1 += str(i) + " "
	return tmp1

def printToFile(arr):
	myf = open("test2.pbm","w")
	myf.write("P1\n100 100\n")
	for i in arr:
		myf.write(ArrToString(i))
	myf.close()

printToFile(bigy)
