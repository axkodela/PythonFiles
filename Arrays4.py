def mkArray1():
	x = []
	for n in range(101):
		x.append(n)
	return x
print("Evens:")
print(mkArray1()[::2])

print("\nOdds:")
print(mkArray1()[1::2])

print("--------------------------------------------------------------------------------------------------------------------------------------")

## Python Exercise #2.
print("\nReverse:")
def mkArray2():
	x = []
	for n in range(101):
		x.append(n)
	return x
print(mkArray2()[::-1])

print("---------------------------------------------------------------------------------------------------------------------------------------")

## Python Excersize #3.
import random
def mkArray3():
	x = []
	for n in range(4):
		x.append(random.randint(0,100))
	return x

biga = []
sum = 0

for n in range(10):
	biga.append(mkArray3())
	
for n in biga:
	sum = 0
	for x in n:
		sum+=x
	print(n, str(sum))
