for line1, line2 in zip(open('col1.txt'), open('col2.txt')):
    print('{}\t{}'.format(line1.rstrip('\n'), line2.rstrip('\n')))

# paste col1.txt col2.txt
