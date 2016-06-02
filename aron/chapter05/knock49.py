# knock49.py
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
def getCommonMinNode(setA, setB):
	pass
def main():
	lineNo = 0
	for sentenceData in knock41.sentenceDataIterator(sys.stdin):
		chunkList = knock41.createChunkListFromData(sentenceData)

		for j in range(1, len(chunkList)):
			if(chunkList[j].hasNone()):
				for i in range(0, j):
					if(chunkList[i].hasNone()):
						pathI = getPathToRoot(chunkList, i)
						pathJ = getPathToRoot(chunkList, j)
						if j in pathI:
							pathI = pathI[0 : pathI.index(j) + 1]
							first = chunkList[i].origin("X")
							last  = chunkList[j].origin("Y")
							pathSurface = [chunkList[i].origin() for i in pathI[1:-1]]
							pathSurface.insert(0, first)
							pathSurface.append(last)
							print ("->".join(pathSurface))
						else:
							for k in pathJ[1:]:
								if(k in pathI):
									pathSurfaceI = [chunkList[idx].origin() for idx in pathI[1:pathI.index(k)]]
									pathSurfaceI.insert(0, chunkList[i].origin("X"))

									pathSurfaceJ = [chunkList[idx].origin() for idx in pathJ[1:pathJ.index(k)]]
									pathSurfaceJ.insert(0, chunkList[j].origin("Y"))

									path_I_To_PrevK = "->".join(pathSurfaceI)
									path_J_To_prevK = "->".join(pathSurfaceJ)
									print ("%s|%s|%s" % (path_I_To_PrevK, path_J_To_prevK, chunkList[k].origin()))
									break
						# else:
						# 	print ("->".join([chunkList[idx].origin() for idx in pathI]))
						# 	print ("->".join([chunkList[idx].origin() for idx in pathJ]))
						# getCommonNode()


		lineNo += 1

if __name__ == '__main__':
	main()