def ngram(seq, n):
    return zip(*[seq[i:] for i in range(n)])

s = 'I am an NLPer'
print(list(ngram(s.split(), 2)))
print(list(ngram(s, 2)))
