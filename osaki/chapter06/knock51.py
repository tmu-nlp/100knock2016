from knock50 import mkline
import re
import sys

def mkword(sentence):
    result=""
    for word in sentence.split(" "):
        result+=word+"\n"
    return(result)

if __name__=='__main__':
    for line in open(sys.argv[1]):
        for sentence in mkline(line).strip("\n").split("\n"):
            print(mkword(sentence))
