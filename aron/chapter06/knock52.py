# knock52.py 
from stemming.porter2 import stem
import sys

if __name__ == '__main__':
	for line in sys.stdin:
		word = line.strip()
		if(len(word) > 0):
			print ("%s : %s" % (word, stem(word)))
		else :
			print ()

# python3 knock50.py nlp.txt | python3 knock51.py | python3 knock52.py