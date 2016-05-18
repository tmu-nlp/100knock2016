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
    if (count == 0 or count == 2) and line["pos"] == u"名詞":
        ans += line["surface"]
        count += 1
    elif line["pos"] == u"助詞" and line["base"] == u"の":
        ans += line["surface"]
        count += 1
    elif count == 1 and line["pos"] == u"名詞":
        ans = line["surface"]
    else:
        ans = ""
        count = 0
    
    if count >= 3:
        print (ans)
        ans = line["surface"]
        count = 1
