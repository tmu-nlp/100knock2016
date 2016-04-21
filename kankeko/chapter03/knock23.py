#!-*-coding:utf-8-*-

import json
import re


pattern = "==(.+)=="
f = open("jawiki-country.json", 'r')
for line in f:
   dict = json.loads(line)
   if dict["title"] == u"イギリス":
       dict = dict["text"].split()
       for text in dict:
           match = re.search(pattern , text)
           if match:
               count = str(text.count('='))
               count = int(int(count)/2 - 1)
               text = re.sub("=","",text)
               print(count,text)






