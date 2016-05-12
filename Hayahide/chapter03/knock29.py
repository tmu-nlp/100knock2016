#-*- coding: utf-8 -*-
import json
import requests
import re

for line in open("jawiki-country.json", "r"):
    uk = json.loads(line)
    if uk["title"] == u"イギリス":
        break

for line in uk["text"].split("\n"):
    if re.search(r".+ = .+", line):
        word = line.strip("|").split(" = ")
        if word[0] == "国旗画像":
            file_name = word[1]
            break

endpoint = "http://en.wikipedia.org/w/api.php"
params = {'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url', 'format': 'json', 'titles': 'File:{}'.format(file_name)}

response = requests.get(endpoint, params=params)
dic = response.json()

print (dic["query"]["pages"]["23473560"]["imageinfo"][0]["url"])

