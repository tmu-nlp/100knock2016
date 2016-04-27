# knock11.py

import sys

my_file = open('hightemp.txt', "r")
ls = list()
for line in my_file:
	ls.append( line.replace("\t", "_").strip())
	# print line
print ("\n".join(ls))




# linux command:
# not work
# sed  -E 's/\\t/_/g' hightemp.txt 

# work
# http://qiita.com/kyanagimoto/items/37cc8e7a242ca2d1a29e
# sed -E 's/[        ]+/_/g' hightemp.txt