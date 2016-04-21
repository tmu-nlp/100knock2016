import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."

ans = []
words = s.split()
for word in words:
    if len(word) > 4:
        left = word[0]
        right = word[len(word) - 1]
        middle = list(word[1:len(word) - 1])
        random.shuffle(middle)
        ans.append(left + "".join(middle) + right)

    else:
        ans.append(word)

ans = " ".join(ans)

print(ans)

