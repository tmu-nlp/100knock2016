import json

wiki_json = open('jawiki-country.json')

for line in wiki_json:
    dct = json.loads(line)
    if dct["title"] == u'イギリス':
        print(dct["text"])

