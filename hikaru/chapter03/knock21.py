#-*-coding: utf-8-*-
import json, re
f = open('jawiki-country.json','r')
for line in f:
    jsonData = json.loads(line)
    if jsonData['title'] == "イギリス":
        break #ここで抜ければjsonDataにはイギリスの記事しか入ってない、辞書型

UK_list = jsonData['text'].splitlines()
for (i, line) in enumerate(UK_list):
    if re.search("\[\[Category:(.*)", line):
        #print (i+1)
        print (line)
