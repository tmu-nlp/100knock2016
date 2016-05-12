# -*- coding: utf-8 -*-


# 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマーク
# アップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

import re
import pprint

template = {}

for line in open('wiki_uk.txt'):
    markup = re.match('\|(?P<key>.*) = (?P<value>.*)', line)
    if markup:
        value = markup.group('value').replace("'", "").replace("[", "").replace("]", "")
        template[markup.group('key')] = value

pprint.pprint(template)
