import re


def person():
    for line in open('nlp.txt.xml'):
        wrd = re.search(r'<word>(?P<wrd>.+)</word>', line)
        ner = re.search(r'<NER>PERSON</NER>', line)
        if wrd:
            w = wrd.group('wrd')
        if ner:
            print(w)


if __name__ == '__main__':
    person()
