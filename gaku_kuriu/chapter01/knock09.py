def randomize(w):
    import random
    bag = [x for x in range(1, len(w)-1)]
    answer = ''
    for i in range(len(w)):
        if (i==0 or i==len(w)-1):
            answer += w[i]
        else:
            temp = random.choice(bag)
            bag.remove(temp)
            answer += w[temp]
    return(answer)
    
def typoglycemia(s):
    answer_list = []
    for w in s.split(' '):
        if len(w) > 4:
            answer_list.append(randomize(w))
        else:
            answer_list.append(w)
    return(' '.join(answer_list))


s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print('default:', s)
print('Typoglycemia:', typoglycemia(s))
