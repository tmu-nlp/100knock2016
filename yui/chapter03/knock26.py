# -*- coding: utf-8 -*-


# 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
#（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
#（参考: マークアップ早見表）．

import re
import pprint

template = {}

for line in open('wiki_uk.txt'):
    markup = re.match('\|(?P<key>.*) = (?P<value>.*)', line)
    if markup:
        value = markup.group('value').replace("'", "")
        template[markup.group('key')] = value
        
pprint.pprint(template)
