import json
import re

wiki_json = open('json_wiki.txt')
category = re.compile('\[\[Category\:(.*)\]\]')
for line in wiki_json:
    result = category.match(line)
    if result is not None:
        print(result.group(1))

