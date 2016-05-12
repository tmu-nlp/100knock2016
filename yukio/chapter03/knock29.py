# -*- coding: utf-8 -*-

import json
import re
import requests

text = ""
template = {}

for line in open("jawiki-country.json", "r"):
    data = json.loads(line)
    if data["title"] == "イギリス":
        text += data["text"]

target = 0
for line in text.split("\n"):
    if re.search("{{基礎情報", line):
        target = 1
    if target == 1:
        if re.search("\|.+ = .+", line):
            line = line.strip("|")
            ans = line.split(" = ")
            template[ans[0]] = ans[1]
        if re.match("}}", line):
            break

file_name = template["国旗画像"]
endpoint = "https://en.wikipedia.org/w/api.php"
params = {"action": "query", "prop": "imageinfo", "iiprop": "url", "format": "json", "titles": "File:{}".format(file_name)}

response = requests.get(endpoint, params = params)
dic = response.json()

print(dic["query"]["pages"]["23473560"]["imageinfo"][0]["url"])
