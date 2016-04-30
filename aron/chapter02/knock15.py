# knock15.py

import sys

# my_file = open(sys.argv[1], "r")
my_file = open('hightemp.txt', "r")

tail = int(sys.argv[1])

line_list = list()
for line in  my_file:
	line_list.append(line.strip())

print("\n".join(line_list[-tail :]))

# tail -2 hightemp.txt


# list = [1] * 5 = [1,1,1,1,1]