#!-*-coding:utf-8-*-

import json
import re


pattern = "File(.+)\."
f = open("jawiki-country.json", 'r')
for line in f:
   dict = json.loads(line)
   if dict["title"] == u"イギリス":
       dict = dict["text"].split()
       for text in dict:
           match = re.search(pattern , text)
           if match:
               text = re.sub("\|(.+)","",text)
               text = re.sub("\[\[File:","",text)
               print(text)







