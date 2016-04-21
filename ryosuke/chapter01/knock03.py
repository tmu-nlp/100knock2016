s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
lens = [len(tok.replace('.', '').replace(',', '')) for tok in s.split()]
print(lens)
