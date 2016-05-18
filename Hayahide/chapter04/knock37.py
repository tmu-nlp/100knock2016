#-*- coding: utf-8 -*-
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

neko_list = []
for line in open("neko.txt.mecab", "r"):    
    if line == "EOS\n":
        neko_dict = {"surface": line, "base": "EOS", "pos": "EOS", "pos1": "EOS"}
    else:    
        line = line.replace("\t", ",")
        word = line.split(",")
        neko_dict = {"surface": word[0], "base": word[7], "pos": word[1], "pos1": word[2]}
    neko_list.append(neko_dict)

word_dict = defaultdict(int)
for line in neko_list:
    if line["base"] != "EOS":
        word_dict[line["base"]] += 1

count = 0
rank_key = []
rank_value = []
for key, value in sorted(word_dict.items(), key = lambda x:x[1], reverse = True):
    if count >= 10:
        break
    rank_key.append(key)
    rank_value.append(value)
    count += 1

prop = fm.FontProperties(fname = "/Library/Fonts/Osaka.ttf")
plt.bar(range(len(rank_value)), rank_value, align = "center")
plt.xticks(range(len(rank_key)), rank_key, fontproperties = prop)
plt.show()    
