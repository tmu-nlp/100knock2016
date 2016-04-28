# knock19.py
import sys
from collections import defaultdict

my_dict = defaultdict(lambda: 0)
my_file = open('hightemp.txt', "r")

for line in my_file:
	my_dict[line.split()[0]] += 1

sortedDic = sorted(my_dict, key = lambda x:x[1], reverse = True)
for k in sortedDic:
	print (my_dict[k], k)



# cat hightemp.txt | cut -f1 | sort| uniq -c | sort -r