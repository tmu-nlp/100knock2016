from knock20 import getUKtext
import re


category_re = re.compile('(Category:(?P<name1>.+?)\|)|(Category:(?P<name2>.+?)])')
for line in getUKtext().split('\n'):
    match = category_re.search(line)
    if match is not None:
        name1 = match.group('name1')
        name2 = match.group('name2')
        print(name1 if name2 is None else name2)
