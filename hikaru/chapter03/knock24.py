#-*-coding: utf-8-*-
import json, re
f = open('jawiki-country.json','r')
for line in f:
    jsonData = json.loads(line)
    if jsonData['title'] == "イギリス":
        break #ここで抜ければjsonDataにはイギリスの記事しか入ってない、辞書型

UK_text = jsonData['text'].strip()

File_list = re.findall('[File|ファイル]:(.*?)\|', UK_text)
for line in File_list:
    print (line)
#print (File_list)
