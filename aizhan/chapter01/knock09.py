from random import shuffle
S = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

L = S.split()
n = ''
newlist = []

for w in L:
    if len(w)>4:
        nf = ''
        nl = ''
        ncen = ''
        nc = []
        nf = w[0]
        nc = list(w[1:-1])
        shuffle(nc)
        ncen = ''.join(nc)
        nl = w[-1]
        n = nf + ncen + nl
    else:
        n = w
    newlist.append(n)

print(' '.join(newlist))

