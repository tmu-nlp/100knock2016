# -*- coding: utf-8 -*-


# カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import json
import re

for line in open("wiki_uk_category.txt", "r"):
    extract_name = re.search('Category:(?P<name>.*)]]',line)
    if extract_name:
        print(extract_name.group('name'))
