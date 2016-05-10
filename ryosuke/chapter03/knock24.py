from knock20 import getUKtext
import re

re_file = re.compile('ファイル:(?P<name>.+?)\|')
for line in getUKtext().split('\n'):
    match = re_file.search(line)
    if match is not None:
        print(match.group('name'))

