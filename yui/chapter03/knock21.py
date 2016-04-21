# -*- coding: utf-8 -*-


# カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import json

f = open("jawiki-country.json", "r")

for json_line in f.readlines():
    a = json.loads(json_line)
    print a.category(unichr)
