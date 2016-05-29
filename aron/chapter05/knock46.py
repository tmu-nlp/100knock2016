# knock46.py
###############################################
# 46. 動詞の格フレーム情報の抽出
# 
# 45のプログラムを改変し，述語と格パターンに続けて項
# （述語に係っている文節そのもの）をタブ区切り形式で
# 出力せよ．45の仕様に加えて，以下の仕様を満たすよう
# にせよ．
# 
# 項は述語に係っている文節の単語列とする（末尾の助詞を
# 取り除く必要はない）
# 述語に係る文節が複数あるときは，助詞と同一の基準・
# 順序でスペース区切りで並べる
# 「吾輩はここで始めて人間というものを見た」という例文
# （neko.txt.cabochaの8文目）を考える． この文は
# 「始める」と「見る」の２つの動詞を含み，「始める」に
# 係る文節は「ここで」，「見る」に係る文節は「吾輩は」
# と「ものを」と解析された場合は，次のような出力になる
# はずである．
# 
# 始める  で      ここで
# 見る    は を   吾輩は ものを
###############################################

import sys, re
import knock41

def main():
	# for sentData in knock41.
	for sentenceData in knock41.sentenceDataIterator(sys.stdin):
		chunkList = knock41.createChunkListFromData(sentenceData)
		for c in chunkList:
			if c.hasVerb():
				# output = ""
				baseVerb = c.getMorph(c.firstVerbId())._base
				joshi = list()
				joshiChunk = list()
				for srcId in c.sources():
					# print(c.origin(), c.firstVerbId())
					id_joshi = chunkList[int(srcId)].getJoshiId()

					# print (id_joshi)
					if id_joshi != -1 :
						baseJoshi = chunkList[int(srcId)].getMorph(id_joshi)._base
						joshi.append(baseJoshi)
						joshiChunk.append(chunkList[int(srcId)].origin())
				if len(joshi) > 0 :
					print("%s\t%s\t%s" % (baseVerb, " ".join(joshi), " ".join(joshiChunk)))

if __name__ == '__main__':
	main()