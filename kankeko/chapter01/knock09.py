#coding: utf-8

import random

test = raw_input()
test = test.split()
answer = []

for i in test:
    if len(i) > 4:
        a1 = i[0]
        a2 = i[len(i)-1]
        l = list(i[1:len(i)-1])
        random.shuffle(l)
        l = "".join(l)
        answer.append(a1 + l + a2)
    else:
        answer.append(i)
answer = " ".join(answer)
print answer
        
        


