#-*-coding: utf-8-*-
import json, re
f = open('jawiki-country.json','r')
for line in f:
    jsonData = json.loads(line)
    if jsonData['title'] == "イギリス":
        break #ここで抜ければjsonDataにはイギリスの記事しか入ってない、辞書型

UK_text = jsonData['text'].strip()
print (type(UK_text))
#for line in UK_list:
#    print (line)
   # search = re.match('Category:(.*)', line)
   # print (search.string)    
#search = re.search('Category:(.*)', UK_list)
print (re.findall('Category:(.*?)\]\]', UK_text))
