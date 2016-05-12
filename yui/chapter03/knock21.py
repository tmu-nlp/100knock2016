# -*- coding: utf-8 -*-


# カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import json
import re

for line in open("wiki_uk.txt", "r"):
    extract_category = re.search(r"Category", line)
    if extract_category:
        print(line)
