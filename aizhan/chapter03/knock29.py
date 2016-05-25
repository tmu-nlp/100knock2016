import re
import pprint
import requests
file_name = 'Flag of the United Kingdom.svg'
endpoint = 'https://en.wikipedia.org/w/api.php'
params = {'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url', 'format': 'json', 'titles': 'File:{}'.format(file_name)}
response = requests.get(endpoint, params=params)
dic = response.json()

for line in dic.values():
    result = re.search(r"'url': '(?P<pngurl>.*?)'", str(line))
    if result:
        print(result.group('pngurl'))

