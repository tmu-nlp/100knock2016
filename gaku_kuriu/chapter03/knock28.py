import sys, re

ansdict = {}

def filter(s):
    if re.search('\[{2}.*\]{2}', s):
        if re.search('\[{2}(.*?)\|(.*?)\]{2}', s):
            s = re.sub('\[{2}[^\[\]]*?\|(.*?)\]{2}', '\\1', s)
        else:
            s = re.sub('\[{2}(.*?)\]{2}', '\\1', s)
        return(filter(s))
    else:
        return(s)

with open(sys.argv[1], 'r') as rf:
    s = rf.read()
    splits = re.split('\n[\|\}]', s)
    for sp in splits:
        result = re.search('(.*)\s\=\s(.*)', sp, re.DOTALL)
        if result != None:
            ansdict[result.group(1)] = filter(re.sub("['{2}'{3}'{5}]", '', result.group(2)))

for k, v in ansdict.items():
    print(k, v)
