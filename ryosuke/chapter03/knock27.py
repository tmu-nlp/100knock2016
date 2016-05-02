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


def replace(s):
    def sn(n):
        def replace_n(m):
            for i in range(1, n + 1):
                tmp = m.group('s{}'.format(i))
                if tmp is not None:
                    return tmp
        return replace_n
    tmp = re_highlight.sub(sn(2), s)
    tmp = re_inlink.sub(sn(3), tmp)
    return tmp

re_base_info = re.compile('\|(?P<key>.+?) = (?P<value>.+)')
re_highlight = re.compile('\'\'\'\'(?P<s1>.+?)\'\'\'\'|\'\'\'(?P<s2>.+?)\'\'\'')
re_inlink = re.compile('\[\[.+?#.+?\|(?P<s1>.+?)\]\]|\[\[.+?\|(?P<s2>.+?)\]\]|\[\[(?P<s3>.+?)\]\]')
base_info = dict()
for line in getUKtext().split('\n'):
    if in_base_info(line):
        match = re_base_info.search(line)
        if match is not None:
            key = replace(match.group('key'))
            value = replace(match.group('value'))
            base_info[key] = value

for k, v in base_info.items():
    print(k, ':', v)
