S = "I am an NLPer"

def ngram(some_s):
    T_bgram = []
    M_bgram = []
    T = some_s.split()
    M = list(some_s)

    for i in range(len(T)-1):
        T_bgram.append([T[i],T[i+1]])

    for i in range(len(M)-1):
        M_bgram.append([M[i],M[i+1]])

    print('単語bi-gram: ', T_bgram)
    print('文字bi-gram: ', M_bgram)

ngram(S)

