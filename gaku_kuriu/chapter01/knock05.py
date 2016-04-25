def ngram(s, n):
    ngrams = []
    for i in range(len(s)-(n-1)):
        ngrams.append(s[i:i+n])
    return(ngrams)

s = 'I am an NLPer'
words = s.split(' ')

print('単語bi-gram: ', ngram(words, 2))
print('文字bi-gram: ', ngram(s, 2))

