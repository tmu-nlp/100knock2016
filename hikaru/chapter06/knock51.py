from knock50 import getsentence
import re
import sys #int(sys.argv[1])

def getword():
    text = getsentence()
    line_list = text.split('\n')
    ans = list()
    for line in line_list:
        word_list = line.split(' ')
        for word in word_list:
            ans.append(word)
        ans.append(' ')
    return  ans

if __name__ == "__main__":
    word_list = getword()
    for word in word_list:
        print (word)
