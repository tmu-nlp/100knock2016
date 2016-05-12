import re

for line in open('json_wiki.txt'):
    result = re.search(r'Category:(?P<categname>.*)]]',line)
    if result:
        print(result.group('categname'))

