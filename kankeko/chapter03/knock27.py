#-*-coding:utf-8-*-

import json
import re


a = 0
pattern1 = u"基礎情報"
pattern2 = u"}}"
pattern3 = u"\|"
mydict = {}
f = open("jawiki-country.json", 'r')
for line in f:
    edict = json.loads(line)
    if edict["title"] == u"イギリス":
        kaneko = edict["text"].split("\n")
        for text in kaneko:
            if re.search(pattern1, text):
                a = 1
            if re.match(pattern2, text):
                break
            if a == 1 and re.match(pattern3, text):
                mylist = text.split(" = ")
                print(mylist)
                mylist[0] = mylist[0].replace("|","")
                mylist[1] = mylist[1].replace("]","")
                mylist[1] = re.sub("\[.+\|","",mylist[1])
                mylist[1] = mylist[1].replace("[[","")
                mydict[mylist[0]] = mylist[1]
        for key, value in mydict.items():
            print(key,value)
