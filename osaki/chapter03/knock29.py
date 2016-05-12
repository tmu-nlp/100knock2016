import requests
import re

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict
d=defaultdict(lambda:0)
import json
s=""
t=""
c=1000000
f=open("jawiki-country.json","r")
for line in f.readlines():
    data=json.loads(line)
    if data["title"]==u"イギリス":
        s=data["text"]

for line in s.split("\n"):
    for w in line:
        if w=="{":
            c+=1
        elif w=="}":
            c-=1
    if c==0:
        break
    if c<1000000:
        t=t+line+"\n"
    if line.startswith(u"{{基礎情報"):
        c=2
t=t.strip("|").strip("\n")

for line in t.split("\n|"):
    d[line.split(" = ")[0]]=line.split(" = ")[1].replace("'''''","").replace("'''","").replace("''","")

for foo,bar in d.items():
    d[foo]=bar.replace("[","").replace("]","")

file_name = d[u"国旗画像"]
endpoint = 'https://en.wikipedia.org/w/api.php'
params = {'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url', 'format': 'json', 'titles': 'File:{}'.format(file_name)}

response = requests.get(endpoint, params=params)
dic = response.json()

for word in dic.values():
    s=str(word)
    a=re.search(r"'url': '(?P<myurl>.*?)'",s)
    if a:
        print(a.group("myurl"))
