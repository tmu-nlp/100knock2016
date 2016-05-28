# coding = utf-8
# knock43.py

################################################
# 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
# 
# 名詞を含む文節が，動詞を含む文節に係るとき，これらを
# タブ区切り形式で抽出せよ．ただし，句読点などの記号は
# 出力しないようにせよ.
################################################



import sys, re
import knock41

def main():
	# data = []
	for sentenceData in knock41.sentenceDataIterator(sys.stdin):
		chunkList = knock41.createChunkListFromData(sentenceData)
		# data = []
		for c in chunkList:
			if c.hasNone() and -1 < c.dest() < len(chunkList) and chunkList[c.dest()].hasVerb():
				print ("%s\t%s" % (c.origin(), chunkList[c.dest()].origin()))
			# print(c.origin().strip(), "\t", ())

			
if __name__ == '__main__':
	main()