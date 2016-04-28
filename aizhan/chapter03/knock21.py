import json
import re

wiki_json = open('json_wiki.txt')
category = re.compile('\[\[Category\:.*\]\]')
for line in wiki_json:
    if category.match(line) is not None:
        print(line.strip())
        
