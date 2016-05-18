# -*- coding: utf-8 -*-


# セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

import re

for line in open('wiki_uk.txt'):
    section = re.match(r'=+.*=+', line)
    if section:
        level = int(line.count('=')/2-1)
        print(line, level)
