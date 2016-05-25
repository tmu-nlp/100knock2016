from knock20 import getUKtext
import re


def in_base_info(line):
    if not hasattr(in_base_info, 'bool'):
        in_base_info.bool = False
    if line.startswith('{{基礎情報'):
        in_base_info.bool = True
    elif line.startswith('}}'):
        in_base_info.bool = False
    return in_base_info.bool


re_base_info = re.compile('\|(?P<key>.+?) = (?P<value>.+)')
base_info = dict()
for line in getUKtext().split('\n'):
    if in_base_info(line):
        match = re_base_info.search(line)
        if match is not None:
            base_info[match.group('key')] = match.group('value')

for k, v in sorted(base_info.items()):
    print(k, ':', v)
