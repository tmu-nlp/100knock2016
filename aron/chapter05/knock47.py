# knock47.py
# 47. 機能動詞構文のマイニング
# 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

# 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
# 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
# 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
# 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
# 例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

# 返事をする      と に は        及ばんさと 手紙に 主人は
# このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

# コーパス中で頻出する述語（サ変接続名詞+を+動詞）
# コーパス中で頻出する述語と助詞パターン

import sys, re
import knock40, knock41

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
				idWoChunk = -1
				idWoMorph = -1
				for srcId in c.sources():
					# print(c.origin(), c.firstVerbId())
					id_joshi = chunkList[int(srcId)].getJoshiId()

					# print (id_joshi)
					if id_joshi != -1 :
						baseJoshi = chunkList[int(srcId)].getMorph(id_joshi)._base
						if baseJoshi == "を":
							idWoChunk = int(srcId)
							idWoMorph = id_joshi
						else:
							joshi.append(baseJoshi)
							joshiChunk.append(chunkList[int(srcId)].origin())
				if len(joshi) > 0 and idWoChunk >= 0 :
					morph = chunkList[idWoChunk]._morphs[idWoMorph - 1]
					# pos = 
					if(morph.pos1() == "サ変接続"):
						print("%s%s\t%s\t%s" % (chunkList[idWoChunk].origin(), baseVerb, " ".join(joshi), " ".join(joshiChunk)))

if __name__ == '__main__':
	main()