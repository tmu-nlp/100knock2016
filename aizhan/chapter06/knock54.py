import re


def tagging():
    w, l, p = [], [], []
    for line in open('nlp.txt.xml'):
        wrd = re.search(r'<word>(?P<wrd>.+)</word>', line)
        lem = re.search(r'<lemma>(?P<lem>.+)</lemma>', line)
        pos = re.search(r'<POS>(?P<pos>.+)</POS>', line)
        if wrd:
            w.append(wrd.group('wrd'))
        if lem:
            l.append(lem.group('lem'))
        if pos:
            p.append(pos.group('pos'))
    for token in zip(w, l, p):
        print(*token, sep='\t')


if __name__ == '__main__':
    tagging()
