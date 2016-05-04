import sys, re

ansdict = {}

with open(sys.argv[1], 'r') as rf:
    s = rf.read()
    splits = re.split('\n[\|\}]', s)
    for sp in splits:
        result = re.search('(.*)\s\=\s(.*)', sp, re.DOTALL)
        if result != None:
            ansdict[result.group(1)] = re.sub("['{2}'{3}'{5}]", '', result.group(2))

for k, v in ansdict.items():
    print(k, v)
