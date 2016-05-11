import requests
import re

file_name = 'Flag_of_the_United_Kingdom.svg'
endpoint = 'https://en.wikipedia.org/w/api.php'
params = {'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url', 'format': 'json', 'titles': 'File:{}'.format(file_name)}

response = requests.get(endpoint, params=params)
dic = response.json()

for word in dic.values():
    s=str(word)
    a=re.search(r"'url': '(?P<myurl>.*?)'",s)
    if a:
        print(a.group("myurl"))
