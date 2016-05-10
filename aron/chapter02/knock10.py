# knock10.py
import sys

my_file = open('hightemp.txt', "r")

line_count = 0
for line in my_file:
	if(line[-1] == '\n'):
		line_count += 1
print (line_count)

# linux command:
# wc -l "hightemp.txt"