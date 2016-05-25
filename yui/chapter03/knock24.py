# -*- coding: utf-8 -*-


# ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

import re

for line in open('wiki_uk.txt'):
    media = re.search('File:(?P<file_name>.+\..{3})?\|', line)
    if media:
        print(media.group('file_name'))
