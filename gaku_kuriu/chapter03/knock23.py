import sys, re

with open(sys.argv[1], 'r') as rf:
    for line in rf:
        result = re.search('^(=+)\s*(.*?)\s*(=+)$', line)
        if result != None:
            print(result.group(2), 'レベル:'+str(len(result.group(1)) - 1))
