import re

re_sent_end = re.compile('(?P<end>\.|\;|\:|\?|\!) (?P<start>[A-Z])')
for line in open('nlp.txt'):
    line = line.rstrip('\n')
    if line == '':
        continue
    print(re_sent_end.sub(lambda m: m.group('end') + '\n' + m.group('start'), line))
