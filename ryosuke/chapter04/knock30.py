def get_sentences():
    sentence = list()
    for line in open('neko.txt.mecab'):
        if line.startswith('EOS'):
            if len(sentence) != 0:
                yield sentence
                sentence = list()
        else:
            surface = line.split('\t')[0]
            base = line.split('\t')[1].split(',')[6]
            pos = line.split('\t')[1].split(',')[0]
            pos1 = line.split('\t')[1].split(',')[1]
            morph = dict()
            morph['surface'] = surface if surface != '*' else ''
            morph['base'] = base if base != '*' else ''
            morph['pos'] = pos if pos != '*' else ''
            morph['pos1'] = pos1 if pos1 != '*' else ''
            sentence.append(morph)


if __name__ == '__main__':
    for sentence in get_sentences():
        for morph in sentence:
            print(morph)
        print('EOS')
