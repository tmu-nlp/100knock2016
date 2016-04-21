S1 = "paraparaparadise"
S2 = "paragraph"

def bigram(some_s):
    newset = set()
    newstr = ''
    for i in range(1,len(some_s)):
        newstr = some_s[i-1] + some_s[i]
        newset.add(newstr)
        newstr = ''

    return newset

X = bigram(S1)
Y = bigram(S2)

print('X: ', X)
print('Y: ', Y)

def washuugou(a,b):
    wsg = a.union(b)
    print('XとYの和集合1: ', wsg)


def sekishuugou(a,b):
    ssg = a.intersection(b)
    print('XとYの積集合: ', ssg)


def sashuugou(a,b):
    sasg = a.difference(b)
    return sasg 


def issein(a):
    se = {'se'}
    if se.issubset(a):
        return True
    else:
        return False


washuugou(X,Y)
sekishuugou(X,Y)
print('XとYの差集合: ', sashuugou(X,Y))
print('YとXの差集合: ', sashuugou(Y,X))
print("'se' in X: ", issein(X))
print("'se' in Y: ", issein(Y))
