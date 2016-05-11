import re
import pprint

template = {}
values = []
for line in open('json_wiki.txt'):
    result = re.match('\|(?P<keys>.*) = (?P<values>.*)',line)
    if result:
        values = result.group('values').replace("'","").replace("[",".").replace("]","")
        template[result.group('keys')] = values

pprint.pprint(template)

