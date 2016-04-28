# kncock12.py

import sys

col = int(sys.argv[1]) - 1
my_file = open('hightemp.txt', "r")

for line in my_file:
	cols = line.split()
	print cols[col]


'''
linux command

cat hightemp.txt | cut -f1 >col1.txt
cat hightemp.txt | cut -f2 >col2.txt

'''

# with