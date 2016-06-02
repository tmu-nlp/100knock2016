import re

def getsentence():
    text = ''
    re_split = re.compile('(?P<syutan>[.;:?!]) (?P<omoji>[A-Z])')

    for lines in open('nlp.txt', 'r'):
        text += re_split.sub(lambda match: match.group('syutan') + '\n' + match.group('omoji'), lines)
    return text

if __name__ == "__main__":
    print (getsentence())