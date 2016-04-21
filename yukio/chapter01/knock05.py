def n_gram(s, n):
    ans = [] 
    for i in range(0, len(s) - n + 1):
        gram = ""
        for j in range(i, i + n - 1):
            gram += s[j]
            gram += "-"
        gram += s[i + n - 1]
        ans.append(gram)
    return(ans)

print(n_gram("I am an NLPer".split(), 2))
print(n_gram("I am an NLPer", 2))
