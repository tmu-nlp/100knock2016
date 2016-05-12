import requests
import json, re
f = open('jawiki-country.json','r')
for line in f:
    jsonData = json.loads(line)
    if jsonData['title'] == "イギリス":
        break 
UK_text = jsonData['text'].strip() 
find_list = re.findall('==+(.*?)==+', UK_text)# + 直前の正規表現の1回以上の繰り返し
                
UK_dict = {}
UK_list = jsonData['text'].splitlines()
for (i, line) in enumerate(UK_list):
    if line.count('='):
        field = re.search('\|(.*?)=', line)
        value = re.search('=(.*)', line)
        if field != None and value != None:
            UK_dict[field.group(1).strip()] = value.group(1).strip()
    if line == '}}':                                                                break

for fi, va in UK_dict.items():
    va = va.replace("'''", '')
    va = re.sub('\[\[|\]\]', '', va)
    #va = re.sub('', va)
    if fi == '国旗画像':
        file_name = va
        break
#file_name = 'Royal_Coat_of_Arms_of_the_United_Kingdom.svg'
#file_name = 'Flag of the United Kingdom.svg'
endpoint = 'https://en.wikipedia.org/w/api.php'
params = {'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url', 'format': 'json', 'titles': 'File:{}'.format(file_name)}

response = requests.get(endpoint, params=params)
dic = response.json()
dic2 = dic['query']
dic3 = dic2['pages']
dic4 = dic3['23473560']
dic5 = dic4['imageinfo']
dic6 = dic5[0]
print (dic6['url'])
#print (dic)

#{'query': {'pages': {'23473560': {'ns': 6, 'imageinfo': [{'url': 'https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg', 'descriptionshorturl': 'https://en.wikipedia.org/w/index.php?curid=23473560', 'descriptionurl': 'https://en.wikipedia.org/wiki/File:Flag_of_the_United_Kingdom.svg'}], 'imagerepository': 'local', 'title': 'File:Flag of the United Kingdom.svg', 'pageid': 23473560}}}, 'batchcomplete': ''}
