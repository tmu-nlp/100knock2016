from knock20 import getUKtext
import re


section_re = re.compile('(?P<section>=+)(?P<name>[^=]+)=+')
for line in getUKtext().split('\n'):
    match = section_re.search(line)
    if match is not None:
        name = match.group('name')
        level = len(match.group('section'))
        if 'http' in name or 'ref' in name:
            continue
        print('level: {}, name: "{}"'.format(level, name))
