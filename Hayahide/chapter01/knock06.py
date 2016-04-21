def make_ngram(s, N):
    ngram = []

    for i in range(len(s) - 1):
        temp = ""
        count = 0

        for j in range(len(s) - 1):
            if s[i + j] != " ":
                temp += s[i + j]
                count += 1
            if count >= N:
                break
        if s[i] != " ":
            ngram.append(temp)

    return ngram

X = set(make_ngram("paraparaparadise", 2))
Y = set(make_ngram("paragraph", 2))

print "X | Y: " + str(X | Y)
print "X - Y: " + str(X - Y)
print "X & Y: " + str(X & Y)

if "se" in X:
    print "X includes 'se'."
if "se" in Y:
    print "Y includes 'se'."             
