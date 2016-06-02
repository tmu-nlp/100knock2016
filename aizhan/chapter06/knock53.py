import re


def tokenization():
    for line in open('nlp.txt.xml'):
        rst = re.search(r'<word>(?P<word>.+)</word>', line)
        if rst and rst.group('word') != ',' and rst.group('word') != '.':
            print(rst.group('word'))


if __name__ == '__main__':
    tokenization()
