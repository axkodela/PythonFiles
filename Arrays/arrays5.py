import random
def mkArray():
	x = []
	for n in range(10):
		x.append(random.randint(0,100))
	return x

biga = []

for n in range(10):
	biga.append(mkArray())

sum = 0
for y in biga:
	sum = 0
	for i in y:
		sum+=i
	print(y, sum)
