from knock30 import neko_mecab

list_n = []

for line in neko_mecab():
    if line['pos'] == '名詞':
        list_n.append(line['surface'])
    else:
        if len(list_n) > 1:
            print(list_n)
        list_n = []