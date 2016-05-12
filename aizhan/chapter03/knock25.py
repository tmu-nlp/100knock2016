import re
import pprint

template = {}

for line in open('json_wiki.txt'):
    result = re.match('\|(?P<keys>.*) = (?P<values>.*)',line)
    if result:
        template[result.group('keys')] = result.group('values')

pprint.pprint(template)

