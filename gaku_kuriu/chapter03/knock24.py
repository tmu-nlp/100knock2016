import sys, re

with open(sys.argv[1], 'r') as rf:
    for line in rf:
        result = re.search('^\[{2}(ファイル|File):(.*?)\|(.*?)\|(.*?)\]{2}$', line)
        if result != None:
            print(result.group(2))
