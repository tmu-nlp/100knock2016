from collections import defaultdict


vocab = defaultdict(int)
for line in open('hightemp.txt'):
    vocab[line.split('\t')[0]] += 1
for key, value in sorted(vocab.items(), key=lambda x: -x[1]):
    print(value, key)

# cut -f1 hightemp.txt| sort | uniq -c| sort -r
