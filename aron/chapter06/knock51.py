# knock51.py
# coding = utf-8
import sys
if __name__ == '__main__':
	for line in sys.stdin:
		wlist = line.split()
		for word in wlist:
			print("%s\n" % (word))