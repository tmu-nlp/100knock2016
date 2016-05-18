#-*-coding: utf-8-*-
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname='/Library/Fonts/Osaka.ttf', size=14)

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
label_list = []
x = []
y = []
for neko in neko_list:
    count_dict[neko['表層形']] += 1 #keyが単語 valueがその単語の出現頻度

hist_dict = defaultdict(int)

#for key, value in count_dict.items(): 
#    hist_dict[value] += 1 #keyが単語の出現頻度 valueが出現頻度の種類数

for key, value in sorted(count_dict.items(), key=lambda x: -x[1]):
    y.append(value)
x = [a for a in range(len(y))]

plt.xscale('log')
plt.yscale('log')
plt.plot(x, y)
#plt.scatter(x, y)
plt.show()
