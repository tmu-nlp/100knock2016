# knock45.py
################################################
# 45. 動詞の格パターンの抽出
# 
# 今回用いている文章をコーパスと見なし，日本語の述語が
# 取りうる格を調査したい．動詞を述語，動詞に係っている
# 文節の助詞を格と考え，述語と格をタブ区切り形式で出力
# せよ． ただし，出力は以下の仕様を満たすようにせよ．
# 
# 動詞を含む文節において，最左の動詞の基本形を述語とす
# る述語に係る助詞を格とする
# 述語に係る助詞（文節）が複数あるときは，すべての助詞
# をスペース区切りで辞書順に並べる
# 「吾輩はここで始めて人間というものを見た」という例文
# （neko.txt.cabochaの8文目）を考える． この文は
# 「始める」と「見る」の２つの動詞を含み，「始める」に
# 係る文節は「ここで」，「見る」に係る文節は「吾輩は」
# と「ものを」と解析された場合は，次のような出力になる
# はずである．
# 
# 始める  で
# 見る    は を
# このプログラムの出力をファイルに保存し，以下の事項を
# UNIXコマンドを用いて確認せよ．
# 
# コーパス中で頻出する述語と格パターンの組み合わせ
# 「する」「見る」「与える」という動詞の格パターン
# （コーパス中で出現頻度の高い順に並べよ）
################################################

# 問題：
# 1文節中助詞複数ある場合がある、その時どう処理する？

import sys, re
import knock41

def main():
	# for sentData in knock41.
	for sentenceData in knock41.sentenceDataIterator(sys.stdin):
		chunkList = knock41.createChunkListFromData(sentenceData)
		for c in chunkList:
			if c.hasVerb():
				# output = ""
				baseVerb = c.getMorph(c.firstVerbId()).base
				joshi = list()
				for srcId in c.sources():
					# print(c.origin(), c.firstVerbId())
					id_joshi = chunkList[int(srcId)].getJoshiId()

					# print (id_joshi)
					if id_joshi != -1 :
						baseJoshi = chunkList[int(srcId)].getMorph(id_joshi).base
						joshi.append(baseJoshi)
				if len(joshi) > 0 :
					print("%s\t%s" % (baseVerb, " ".join(sorted(joshi))))

if __name__ == '__main__':
	main()
