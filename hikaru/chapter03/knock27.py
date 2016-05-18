#-*-coding: utf-8-*-
import json, re
f = open('jawiki-country.json','r')
for line in f:
    jsonData = json.loads(line)
    if jsonData['title'] == "イギリス":
        break 

UK_text = jsonData['text'].strip() 
find_list = re.findall('==+(.*?)==+', UK_text)# + 直前の正規表現の1回以上の繰り返し
#print (find_list)

UK_dict = {}
UK_list = jsonData['text'].splitlines()
for (i, line) in enumerate(UK_list):
    if line.count('='):
        field = re.search('\|(.*?)=', line)
        value = re.search('=(.*)', line)
        if field != None and value != None:
            UK_dict[field.group(1).strip()] = value.group(1).strip()
    if line == '}}':
        break

for fi, va in sorted(UK_dict.items()):
    #va = va.replace("'''", '')
    #va = re.sub('\[\[|\]\]', '', va)
    re_va = re.compile('\[\[[^\[\]]+?\|(?P<s1>[^\[\]]+?)\]\]|\[\[(?P<s2>[^\[\]]+?)\]\]')
    va = re_va.sub(lambda m: m.group('s2') if m.group('s1') is None else m.group('s1'), va)
    print ("field:{} value:{}".format(fi, va))
#print (UK_dict.items())
