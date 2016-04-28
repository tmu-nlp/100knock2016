def ngram(s, n):
    ngrams = []
    for i in range(len(s)-(n-1)):
        ngrams.append(s[i:i+n])
    return(ngrams)

s1 = 'paraparaparadise'
s2 = 'paragraph'
bi_s1 = ngram(s1, 2)
bi_s2 = ngram(s2, 2)
X = set(bi_s1)
Y = set(bi_s2)

print('X:', X)
print('Y:', Y)
print('X | Y:', X | Y)
print('X & Y:', X & Y)
print('X - Y:', X - Y)
print('Y - X:', Y - X)
print('se in X:', 'se' in X)
print('se in Y:', 'se' in Y)
