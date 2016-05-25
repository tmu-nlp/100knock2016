#!-*-coding:utf-8-*-

import json
import re


pattern = "Category"
f = open("jawiki-country.json", 'r')
for line in f:
    dict = json.loads(line)
    if dict["title"] == u"イギリス":
        dict = dict["text"].split()
        for text in dict:
            match = re.search(pattern , text)
            if match:
                text = text.replace("[[Category:","").replace("|","").replace("]","").replace("*","")
                print(text)
