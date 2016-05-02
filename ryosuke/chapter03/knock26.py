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
re_replace = re.compile('\'\'\'\'(?P<s1>.+?)\'\'\'\'|\'\'\'(?P<s2>.+?)\'\'\'')
base_info = dict()
for line in getUKtext().split('\n'):
    if in_base_info(line):
        match = re_base_info.search(line)
        if match is not None:
            key = re_replace.sub(lambda m: m.group('s2') if m.group('s1') is None else m.group('s1'), match.group('key'))
            value = re_replace.sub(lambda m: m.group('s2') if m.group('s1') is None else m.group('s1'), match.group('value'))
            base_info[key] = value

for k, v in base_info.items():
    print(k, ':', v)
