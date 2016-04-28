vocab = set()
for line in open('hightemp.txt'):
    vocab.add(line.split('\t')[0])
print(vocab)

# cut -f1 hightemp.txt| sort | uniq
