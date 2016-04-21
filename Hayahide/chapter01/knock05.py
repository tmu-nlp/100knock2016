def make_ngram(s, N):
    ngram = []
    
    for i in range(len(s) - 1):
        temp = ""
        count = 0
        if s[i] != " ":
            for j in range(len(s) - 1):
                if s[i + j] != " ":
                    temp += s[i + j]
                    count += 1
                if count >= N:
                    break    
            ngram.append(temp)

    return ngram 

s = "I am an NLPer"
N = 2

print make_ngram(s, N)
print make_ngram(s.split(" "), N)
