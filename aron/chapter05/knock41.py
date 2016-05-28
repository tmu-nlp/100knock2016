# knock41.py
# coding = utf-8
import sys, re
import knock40

# * 0 -1D 0/0 0.000000
# * 1 2D 0/1 -0.764522

reChuckHead = re.compile("^\* (?P<id>[0-9]+) (?P<dst>-?[0-9]+)D.*$")

from collections import defaultdict
class Chunk(object):
	"""docstring for Chunk"""
	def __init__(self, id, morph_list, destnitaion, sources):
		super(Chunk, self).__init__()
		self._id = int(id)
		self._morphs = morph_list
		self._dst = int(destnitaion)
		self._srcs = sources

	def id(self):
		return self._id

	def dest(self):
		return self._dst

	# 係り元のリストを返す
	def sources(self):
		return self._srcs

	def appendMorph(self, morph):
		self._morphs.append(morph)

	def __str__(self):
		srcs =",".join(self._srcs)
		bun = ""
		for i, m in enumerate(self._morphs):
			bun += ("\t" + str(m) + ("\n" if( i < len(self._morphs) - 1 ) else ""))
		return "id=%d,des=%d,srcs=[%s]\n%s" % (self._id, self._dst, srcs, bun)

	def origin(self):
		org = ""
		for m in self._morphs:
			org += (m.surface)
			# print (m.surface)
		if org.startswith(" "):
			print ("start with space")
		if org.endswith(" "):
			print ("end with space")
		return org

	# 最初の動詞の添字を返す
	def firstVerbId(self):
		for i, m in enumerate(self._morphs):
			if m.pos == "動詞":
				return i
		return -1

	# 助詞の添字を返す
	def getJoshiId(self):
		for i, m in enumerate(self._morphs):
			if m.pos == "助詞":
				return i
		return -1
	
	# indexに指定された形態素を返す
	def getMorph(self, index):
		if 0 <= index < len(self._morphs):
			return self._morphs[index]
		return None

	def hasNone(self):
		return any(m.pos == "名詞" for m in self._morphs)

	def hasVerb(self):
		return any(m.pos == "動詞" for m in self._morphs)

	

def createMorphFromLine(line):
	return knock40.createMorphFromLine(line)



def createChunkListFromData(data):
	chunkList = []
	srsDict = defaultdict(list)
	for line in data:
		if line.startswith("*"):
			match = reChuckHead.match(line)
			chunkList.append(Chunk(match.group("id"), [], match.group("dst"), srsDict[match.group("id")]))
			if match.group("dst") is not "-1":
				srsDict[match.group("dst")].append(match.group("id"))
		else:
			morph = None
			try:
				morph = createMorphFromLine(line)
			except:
				print("ERR", line)
			else:
				chunkList[len(chunkList) - 1].appendMorph(morph)
	return chunkList

def sentenceDataIterator(input):
	data = []
	for line in input:
		if not line.startswith("EOS"):
			data.append(line)
		else:
			yield data
			data = []

article = []

def main():
	for sdata in sentenceDataIterator(sys.stdin):
			chunkList = createChunkListFromData(sdata)
			article.append(chunkList)

	for chunk in article[7]:
		print ((chunk))

if __name__ == '__main__':
	main()