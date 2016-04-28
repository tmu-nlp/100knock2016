# knock11.py

import sys

my_file = open('hightemp.txt', "r")
ls = list()
for line in my_file:
	ls.append( line.replace("\t", "_").strip())
	# print line
print ("\n".join(ls))


'''

linux command:

# 1.
sed -E 's/[        ]+/_/g' hightemp.txt

# not work
# sed  -E 's/\\t/ /g' hightemp.txt 
# http://qiita.com/kyanagimoto/items/37cc8e7a242ca2d1a29e

2.
cat ./hightemp.txt | tr '\t' ' '

3.
expand -t 1 hightemp.txt


'''