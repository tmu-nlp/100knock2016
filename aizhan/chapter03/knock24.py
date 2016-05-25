import re

for line in open('json_wiki.txt'):
    result = re.search('File:(?P<fname>.+\....)?\|',line)
    if result:
        print(result.group('fname'))
