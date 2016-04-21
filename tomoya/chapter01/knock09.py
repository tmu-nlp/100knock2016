import random
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
t = []
index = []
s = s.split(" ")
for i in range(len(s)):
  if len(s[i]) > 4:
    t.append(s[i])
    index.append(i)
random.shuffle(t)
for i in range(len(t)):
    s[index[i]] = t[i]
print(s)

