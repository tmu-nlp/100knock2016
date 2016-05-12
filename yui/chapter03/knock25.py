# -*- coding: utf-8 -*-


# テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
# 辞書オブジェクトとして格納せよ．

import re
import pprint

template = {}

for line in open('wiki_uk.txt'):
    field_value = re.match('\|(?P<key>.*) = (?P<value>.*)', line)
    if field_value:
        template[field_value.group('key')] = field_value.group('value')
pprint.pprint(template)
