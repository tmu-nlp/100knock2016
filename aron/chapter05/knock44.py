# coding = utf-8
# knock44.py

##################################
# 44. 係り受け木の可視化            
#
# 与えられた文の係り受け木を有向グラフとして可視化せよ．
# 可視化には，係り受け木をDOT言語に変換し，Graphvizを
# 用いるとよい．また，Pythonから有向グラフを直接的に可
# 視化するには，pydotを使うとよい

import sys, re
import knock41
# import graphviz as pgv
from graphviz import Digraph

# def pushData(index, data):

	
def main():
	G = Digraph(format='png')
	# G.attr('node', shape='circle')


	# N = 15    # ノード数

	# # ノードの追加
	# for i in range(N):
	#     G.node(str(i), str(i))

	# # 辺の追加
	# for i in range(N):
	#     if (i - 1) // 2 >= 0:
	#         G.edge(str((i - 1) // 2), str(i))

	# # print()するとdot形式で出力される
	# print(G)

	# # binary_tree.pngで保存
	# G.render('binary_tree')

	data = []
	sentId = 0
	for line in sys.stdin:
		if not line.startswith("EOS"):
			data.append(line)
		else:
			if sentId == int(sys.argv[1]) - 1:
				lst = knock41.createChunkListFromData(data)
				for c in lst:
					if c.dest() != -1:
						G.node(str(c.id()), c.origin())
						G.node(str(c.dest()), lst[c.dest()].origin())
						G.edge(str(c.id()), str(c.dest()))
					# binary_tree.pngで保存
				G.render('knock44', cleanup=True)
				return
			# else:
				
			sentId += 1
			data = []
		
		
if __name__ == '__main__':
	main()