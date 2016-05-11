import re

for line in open('json_wiki.txt'):
    result = re.match(r'(?P<level>=+)(?P<name>.*)=*',line)
    if result:
        level = int(line.count('=')/2-1)
        print(level, line)


