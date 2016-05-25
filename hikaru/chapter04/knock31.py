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
        neko_list.append([my_dict])
        my_dict = {}
for neko in neko_list:
    if neko[0]['品詞'] == '動詞':
        print (neko[0]['表層形'])    

