# knock17.py

import sys

my_file = open('hightemp.txt', "r")
my_set = set()
for line in my_file:
	my_set.add(line.split()[0])

print("\n".join(sorted(my_set)))

# cat hightemp.txt | cut -f1 | sort | uniq 
# | wc -l