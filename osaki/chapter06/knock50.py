import sys
import re

def mkline(line):
    pattern=r'([:;.?!]) ([A-Z])'
    return(re.sub(pattern,lambda x:x.group().replace(" ","\n"),line))

if __name__=='__main__':
    result=""
    for line in open(sys.argv[1]):
        result+=(mkline(line))
        result.strip("\n")
    print(result)
