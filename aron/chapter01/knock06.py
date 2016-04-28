# knock06.py
from collections import defaultdict

strX = "paraparaparadise"
strY = "paragraph"

def biGram(str_in):
	letterBiGram = set()

	for i in range(len(str_in) - 1):
		letterBiGram.add(str_in[i : i+2])
	return letterBiGram

X = biGram(strX)
Y = biGram(strY)

def getUnion(a, b):
	c = a.union(b)
	return c

def getIntersection(a, b):
	c = a.intersection(b)
	return c

def getDifference(a, b):
	c = a.difference(b)
	return c

print (X)
print (Y)
print (getUnion(X, Y))
print (getIntersection(X, Y))
print (getDifference(X, Y))

