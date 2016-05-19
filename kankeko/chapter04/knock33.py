from knock30 import neko_mecab

for line in neko_mecab():
    if line['pos'] == '名詞' and line['pos1'] == 'サ変接続':
        print(line['surface'])
