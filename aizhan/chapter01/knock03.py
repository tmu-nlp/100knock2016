S = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
L = S.split('.')
S = ''.join(L)
L = S.split(',')
S = ''.join(L)
L = S.split()
for w in L:
    print(len(w),sep='',end='')
print()

