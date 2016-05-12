# -*- coding: utf-8 -*-


# 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
#（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに
# 変換すればよい）

import requests
import re

file_name = 'Flag of the United Kingdom.svg'
endpoint = 'https://en.wikipedia.org/w/api.php'
params = {'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url', 'format': 'json', 'titles': 'File:{}'.format(file_name)}
response = requests.get(endpoint, params=params)
dic = response.json()

for line in dic.values():
    flag = re.search(r"'url': '(?P<pngurl>.*?)'", str(line))
    if flag:
        print(flag.group('pngurl'))
