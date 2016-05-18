#-*-coding: utf-8-*-
from collections import defaultdict
#my_dict = defaultdict(lambda:0)
my_dict = {}
neko_list = []
line_list = []
count = 0
for line in open('neko.text.mecab', 'r'):
    line = line.replace('\t', ',')
    line = line.rstrip('\n')
    if line != 'EOS':
        line_list = line.split(',')
        line_list[0] = line_list[0].replace('\u3000', ' ')
        my_dict['表層形'] = line_list[0]
        my_dict['基本形'] = line_list[7]
        my_dict['品詞'] = line_list[1]
        my_dict['品詞細分類'] = line_list[2]
        neko_list.append(my_dict)
        my_dict = {}
n_list = []
for i, neko in enumerate(neko_list):
    if neko['品詞'] == '名詞':
        n_list.append(i)
x = n_list[0]
rensetsu = []
for number in n_list[1:]:
    if x == number - 1: #一文字前の単語が名詞
        rensetsu.append(neko_list[number - 1]['表層形'])#一文字前の単語追加
        rensetsu.append(neko_list[number]['表層形'])#ここだと重複
    else:
        if len(rensetsu) != 0:
            print (sorted(set(rensetsu), key = rensetsu.index))
        rensetsu = []#次の単語は連接じゃないので空に
    x = number
