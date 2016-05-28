# coding = utf-8
# knock43.py

# 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
# 
# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
# ただし，句読点などの記号は出力しないようにせよ．



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
				if c.hasNone() and -1 < c.dest() < len(lst) and lst[c.dest()].hasVerb():
					print ("%s\t%s" % (c.origin(), lst[c.dest()].origin()))
				# print(c.origin().strip(), "\t", ())

			
if __name__ == '__main__':
	main()