import random
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
result = list()
for tok in s.split():
    if len(tok) <= 4:
        result.append(tok)
    else:
        head = tok[0]
        tail = tok[-1]
        middle = tok[1:-1]
        shuffled = ''.join(random.sample(middle, len(middle)))
        result.append(head + shuffled + tail)
print(s)
print(' '.join(result))
