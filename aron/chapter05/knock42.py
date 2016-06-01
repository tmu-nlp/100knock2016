# knock42.py
# coding = utf-8
import sys, re
import knock41

def main():
	data = []
	for sentData in knock41.sentenceDataIterator(sys.stdin):
		chunkList = knock41.createChunkListFromData(sentData)
		# data = []
		for c in chunkList:
			print("%s\t%s" % (
					c.origin().strip(), 
					(chunkList[c._dst].origin().strip() if (c._dst != -1 ) else "NULL")
				))
			# print(c.origin().strip(), "\t", ())

		
if __name__ == '__main__':
	main()