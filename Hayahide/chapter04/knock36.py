#-*- coding: utf-8 -*-
from collections import defaultdict

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

for key, value in sorted(word_dict.items(), key = lambda x:x[1], reverse = True):
    print (key, value) 
