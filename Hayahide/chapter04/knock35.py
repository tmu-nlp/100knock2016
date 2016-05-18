#-*- coding: utf-8 -*-

neko_list = []
for line in open("neko.txt.mecab", "r"):    
    if line == "EOS\n":
        neko_dict = {"surface": line, "base": "EOS", "pos": "EOS", "pos1": "EOS"}
    else:    
        line = line.replace("\t", ",")
        word = line.split(",")
        neko_dict = {"surface": word[0], "base": word[7], "pos": word[1], "pos1": word[2]}
    neko_list.append(neko_dict)

ans = ""
count = 0
for line in neko_list:
    if line["pos"] == u"名詞" and line["base"] != "*\n":
        ans += line["surface"]
        count += 1
    else:
        if count > 1:
            print (ans)
        ans = ""
        count = 0
