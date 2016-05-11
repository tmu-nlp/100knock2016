import re
import pprint

template = {}

for line in open('json_wiki.txt'):
    result = re.match('\|(?P<keys>.*) = (?P<values>.*)',line)
    if result:
        values = result.group('values').replace("'", "")
        template[result.group('keys')] = values


pprint.pprint(template)

