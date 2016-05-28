# knock42.py
# coding = utf-8
import sys, re
import knock41

def main():
	data = []
	for line in sys.stdin:
		if not line.startswith("EOS"):
			data.append(line)
		else:
			lst = knock41.createChunkListFromData(data)
			data = []
			for c in lst:
				print(c.origin(), "\t", (lst[c._dst].origin() if (c._dst != -1 ) else "NULL"))

			
if __name__ == '__main__':
	main()