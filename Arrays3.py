def mkArray(num):
	x = []
	increment = num*4
	for n in range(increment+1,increment+5):
		x.append(n)
	return x

biga = []

for i in range(3):
	biga.append(mkArray(i))

print(biga)
