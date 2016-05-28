# coding = utf-8
# knock44.py

###############################################
# 44. 係り受け木の可視化            
#
# 与えられた文の係り受け木を有向グラフとして可視化せよ．
# 可視化には，係り受け木をDOT言語に変換し，Graphvizを
# 用いるとよい．また，Pythonから有向グラフを直接的に可
# 視化するには，pydotを使うとよい
################################################

import sys, re
import knock41
# import graphviz as pgv
from graphviz import Digraph

# graphviz examples URL:
# http://graphviz.readthedocs.io/en/stable/examples.html

	
def main():
	G = Digraph(format='png')

	for sentId, sentenceData in enumerate(knock41.sentenceDataIterator(sys.stdin)):
		if sentId == int(sys.argv[1]) - 1:
			chunkList = knock41.createChunkListFromData(sentenceData)
			for c in chunkList:
				if c.dest() != -1:
					G.node(str(c.id()), c.origin())
					G.node(str(c.dest()), chunkList[c.dest()].origin())
					G.edge(str(c.id()), str(c.dest()))
				# binary_tree.pngで保存
			G.render('knock44', cleanup=True)
			return		
		
if __name__ == '__main__':
	main()