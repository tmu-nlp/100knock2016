# knock14.py

import sys

# my_file = open(sys.argv[1], "r")
my_file = open('hightemp.txt', "r")

head = int(sys.argv[1])

for i, line in  enumerate(my_file):
	if(i >= head ):
		break
	print (i + 1  ,line.strip())


