def remove_punctuation(s):
    for punc in ['.', ',', ';', ':', '?', '!']:
        if s.endswith(punc):
            return s[:-1]
    return s

for line in open('knock50.txt'):
    spl = line.rstrip('\n').split(' ')
    for tok in spl:
        print(remove_punctuation(tok))
    print()
