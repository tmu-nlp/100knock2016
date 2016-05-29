# knock48.py
# coding = utf-8

import sys, re
import knock41
def getPathToRoot(chunkList, chunkId):
	# print ( "start from %d" % (chunkId))
	pathId=[]
	while -1 < chunkId < len(chunkList):
		pathId.append(chunkId)
		chunkId = chunkList[chunkId].dest()
	return pathId

def main():
	lineNo = 0
	for sentenceData in knock41.sentenceDataIterator(sys.stdin):
		chunkList = knock41.createChunkListFromData(sentenceData)
		# print(lineNo)
		for chunk in chunkList:
			if chunk.hasNone():
				# pathId = []
				pathId = getPathToRoot(chunkList, chunk.id())
				pathSurface = [chunkList[i].origin() for i in pathId]
				print ("->".join(pathSurface))
		lineNo += 1

if __name__ == '__main__':
	main()