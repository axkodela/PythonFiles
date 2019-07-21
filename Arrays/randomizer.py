import random

def randomizer():
	rndm = []
	for n in range(random.randrange(0, 100, 1)):
		rndm.append(n)
	return rndm

randomizer()
