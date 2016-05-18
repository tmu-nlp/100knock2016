# -*- coding: utf-8 -*-


# MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な
# 限り除去し，国の基本情報を整形せよ．

import re
import pprint

template = {}

for line in open('wiki_uk.txt'):
    markup = re.match('\|(?P<key>.*) = (?P<value>.*)', line)
    if markup:
        value = markup.group('value').replace("'", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "")
        template[markup.group('key')] = value

pprint.pprint(template)
