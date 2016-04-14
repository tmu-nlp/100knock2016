def ngram(seq, n):
    return zip(*[seq[i:] for i in range(n)])

t1 = 'paraparaparadise'
t2 = 'paragraph'

X = set(ngram(t1, 2))
Y = set(ngram(t2, 2))
print('X: ', X)
print('Y: ', Y)
print('X | Y: ', X | Y)
print('X & Y: ', X & Y)
print('X - Y: ', X - Y)
print('Y - X: ', Y - X)
print('se in X: ', ('s', 'e') in X)
print('se in Y: ', ('s', 'e') in Y)
