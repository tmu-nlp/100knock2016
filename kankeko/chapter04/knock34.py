from knock30 import neko_mecab

list_mecab = []

for line in neko_mecab():
    list_mecab.append(line)

for i,line in enumerate(list_mecab):
    if line['surface'] == 'の':
        if list_mecab[i-1]['pos'] == '名詞' and list_mecab[i+1]['pos'] == '名詞':
            print(list_mecab[i-1]['surface'] + line['surface'] + list_mecab[i+1]['surface'])