s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
tokens = [tok.replace('.', '').replace(',', '') for tok in s.split()]
lens = [len(tok) for tok in tokens]
print(lens)
