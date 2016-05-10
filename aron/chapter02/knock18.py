# knock18.py
import sys

my_file = open('hightemp.txt', "r")
rows = list()
for line in my_file:
	cols = list()
	for field in line.split():
		cols.append(field)
	rows.append(cols)

for row in sorted(rows, key = lambda x: x[2], reverse=True):
	print ("\t".join(row))

# cat hightemp.txt | cut -f3 | paste - hightemp.txt | sort -r | cut -f2-