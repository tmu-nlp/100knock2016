#-*- coding: utf-8 -*- 

word_count = {}
ans = ""

for s in open("hightemp.txt", "r"):
    words = s.split()
    if words[0] in word_count:
        word_count[words[0]] += 1
    else:
        word_count[words[0]] = 1

for foo, bar in sorted(word_count.items(), key = lambda x : x[1], reverse = True):
    ans += "{} {}\n".format(foo, bar)

print(ans)
