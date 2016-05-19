from knock30 import neko_mecab

for line in neko_mecab():
    if line['pos'] == '動詞':
        print(line['base'])
