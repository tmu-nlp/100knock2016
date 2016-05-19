#-*-coding: utf-8-*-
from collections import defaultdict
import matplotlib.pyplot as plt

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

count_dict = defaultdict(int)
for neko in neko_list:
    count_dict[neko['表層形']] += 1
for key, value in sorted(count_dict.items(), key=lambda x: -x[1]):
    print (value, key)
