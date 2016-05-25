import re

for line in open('json_wiki.txt'):
    result = re.search(r'Category',line)
    if result:
        print(line)
        
