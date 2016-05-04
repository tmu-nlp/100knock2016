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
    #if re.match(strs + "=\w(.*?)==", line):
    if line.count('=='):
        #UK_dict[line] = 1
        #print (re.match('==\w(.*?)==', line))
        #print (re.findall('==(.*?)==', line), "{}".format(level))
        print (re.findall('==+(.*?)==', line), "{}".format(line.count('=')/2 -1))
#print (UK_dict.items())
