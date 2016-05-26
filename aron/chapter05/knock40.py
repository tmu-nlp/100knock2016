#coding = utf-8
import sys
from collections import defaultdict

class Morph(object):
	"""docstring for Morph"""
	def __init__(self, surface, base, pos, pos1, ):
		super(Morph, self).__init__()
		self.surface = surface
		self.base = base  
		self.pos = pos  
		self.pos1 = pos1 
	def printme(self):
		print("surface=%s, base=%s, pos=%s, pos1=%s" % (self.surface, self.base, self.pos, self.pos1))

def createMorphFromLine(line):
	if len(line) == 0 or line[0:3] == "EOS":
		return None
	else:
		words = line.rstrip().replace("\t", ",").split(",")
		# surface:0, pos:1, pos1:2, base:7, 
		return Morph(words[0], words[7], words[1], words[2])

# sentence= []	# 一行, Morph から構成された
article	= [[]] 	# 文章全体、行から構成された

def parseLine(line):
	if line.startswith("EOS"):
		# print(sentence)
		# s = sentence
		article.append([])
		# print (len(article), article[-1])
	else:
		article[-1].append(createMorphFromLine(line))


def main():
	if sys.stdin.isatty() == False:	# 標準入力からの入力
		for line in sys.stdin:
			parseLine(line)
	elif(sys.argv[1] != None):      # 引数からの入力
		with open(sys.argv[1], "r") as inputFile:
			for line in inputFile:
				parseLine(line)
	

	for item in article[2]:
		item.printme()

if __name__ == '__main__':
	main()

# cat neko.txt.cabocha | python3 knock40.py
# python3 knock40.py neko.txt.cabocha
