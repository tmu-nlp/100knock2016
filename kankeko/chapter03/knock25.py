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
           match = re.search(pattern1, text)
           if match:
                a = 1
           if re.match(pattern2, text):
                break
           if a == 1 and re.match(pattern3, text):
                mylist = text.split(" = ")
                mylist[0] = mylist[0].replace("|","")
                mydict[mylist[0]] = mylist[1]
       for key, value in mydict.items():
           print(key, value)
