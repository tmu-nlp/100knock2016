import random

def typoglycemia(s):
    ans = ""
    for i in range(len(s)):
        word = list(s[i])
        if len(word) >= 4:
            head = word.pop(0)
            last = word.pop(-1)
            random.shuffle(word)
            word = "".join(list(head) + word + list(last))
        else:
            word = "".join(word)
        s[i] = word
    
    return " ".join(s)

s = raw_input().split(" ")

print typoglycemia(s)
