import requests
import re

pattern = r"url"
repatter = re.compile(pattern)

file_name = 'Flag_of_the_United_Kingdom.svg'
endpoint = 'https://en.wikipedia.org/w/api.php'
params = {'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url', 'format': 'json', 'titles': 'File:{}'.format(file_name)}
response = requests.get(endpoint, params=params)
dic = response.json()

for words in dic.values():
    w = str(words)
    a = re.search(r"'url': '(?P<myurl>.*?)'",w)
    if a:
        print(a.group("myurl"))
    #for word in words.values():
        #if isinstance(word,dict):
            #for  in word.values():
                #print (key, value)
        #for w in a:
            #print(type(w))
            #print(w)
    #words = words.search("\'url\'(?P<w>.*)?\,")
    #print(w)
    #print(words)
    #print("\n")
