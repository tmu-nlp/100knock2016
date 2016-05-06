#-*-coding: utf-8-*-
import json

f = open('jawiki-country.json', 'r')
for line in f:
    jsonData = json.loads(line)
    for key, value in jsonData.items():
        if key =='title' and "イギリス" in value:
            print(jsonData['text'])
f.close()

