#-*- coding: utf-8 -*-
from collections import defaultdict
import matplotlib.pyplot as plt

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

count_dict = defaultdict(int)
for key, value in word_dict.items():
    count_dict[value] += 1

rank_key = []
rank_value = []
for key, value in sorted(count_dict.items()):
    rank_key.append(key)
    rank_value.append(value)

plt.xscale("log")
plt.yscale("log")
plt.plot(range(len(rank_value)), rank_value)
plt.show()
