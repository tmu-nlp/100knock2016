from knock20 import getUKtext
import re
import requests


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
    tmp = re_file.sub(sn(1), tmp)
    tmp = re_inlink.sub(sn(3), tmp)
    tmp = re_ref.sub(lambda m: '', tmp)
    tmp = re_lang.sub(sn(1), tmp)
    return tmp

re_base_info = re.compile('\|(?P<key>.+?) = (?P<value>.+)')
re_highlight = re.compile('\'\'\'\'(?P<s1>.+?)\'\'\'\'|\'\'\'(?P<s2>.+?)\'\'\'')
re_file = re.compile('\[\[(?P<s1>ファイル:.+?)\|.+?\]\]')
re_inlink = re.compile('\[\[[^\[\]]+?#[^\[\]]+?\|(?P<s1>[^\[\]]+?)\]\]|\[\[[^\[\]]+?\|(?P<s2>[^\[\]]+?)\]\]|\[\[(?P<s3>[^\[\]]+?)\]\]')
re_ref = re.compile('<ref.+?/ref>|<ref.+?/>')
re_lang = re.compile('{{lang\|.+?\|(?P<s1>.+?)}}')
base_info = dict()
for line in getUKtext().split('\n'):
    if in_base_info(line):
        match = re_base_info.search(line)
        if match is not None:
            key = replace(match.group('key'))
            value = replace(match.group('value'))
            base_info[key] = value



name = base_info['国旗画像']
endpoint = 'https://en.wikipedia.org/w/api.php'
params = {'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url', 'format': 'json', 'titles': 'File:{}'.format(name)}
r = requests.get(endpoint, params=params)
d = r.json()
print(d['query']['pages']['23473560']['imageinfo'][0]['url'])
